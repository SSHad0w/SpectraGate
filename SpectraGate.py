import asyncio
import datetime
import argparse

ROUTES = {
    b"SSH-": 2222,
    b"GET ": 80,
    b"POST": 80,
    b"220 ": 21,
    b"\x16\x03": 443,  # TLS
    b"\xff\xfd": 23,   # Telnet
}

LOGFILE = "spectragate.log"
MAX_PEEK = 16

def log_event(ip, protocol, port):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{time}] {ip} → {protocol} → port {port}"
    print(msg)
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")

async def handle_client(reader, writer):
    peer = writer.get_extra_info("peername")[0]

    try:
        data = await reader.readexactly(MAX_PEEK)
    except asyncio.IncompleteReadError:
        writer.close()
        await writer.wait_closed()
        return

    forward_port = None
    matched_proto = "UNKNOWN"
    for sig, port in ROUTES.items():
        if sig in data:
            forward_port = port
            matched_proto = sig.decode(errors='replace').strip()
            break

    if not forward_port:
        writer.close()
        await writer.wait_closed()
        return

    log_event(peer, matched_proto, forward_port)

    try:
        target_reader, target_writer = await asyncio.open_connection("127.0.0.1", forward_port)
        target_writer.write(data)
        await target_writer.drain()
    except Exception:
        writer.close()
        await writer.wait_closed()
        return

    async def pipe(src, dst):
        try:
            while not src.at_eof():
                chunk = await src.read(4096)
                if not chunk:
                    break
                dst.write(chunk)
                await dst.drain()
        except:
            pass
        finally:
            dst.close()

    await asyncio.gather(pipe(reader, target_writer), pipe(target_reader, writer))

async def main():
    parser = argparse.ArgumentParser(description="Project SpectraGate: TCP Protocol Multiplexer")
    parser.add_argument("--port", type=int, default=2345, help="External listening port")
    args = parser.parse_args()

    server = await asyncio.start_server(handle_client, "0.0.0.0", args.port)
    print(f"[SpectraGate] Listening on port {args.port}...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")

