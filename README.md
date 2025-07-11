# SpectraGate

A beginner-friendly banner grabbing lab cloaked in mystery.
One port. Many protocols. No map.

## 🌈 What's This?

**SpectraGate** is a lightweight TCP multiplexer that simulates a world where the traditional link between ports and services is broken. Instead of finding SSH on 22 or HTTPS on 443, students must explore a single exposed port and uncover what’s behind it using only the banners returned and their protocol intuition.

This lab was built to:

* Disrupt the assumption that “port = service”
* Sharpen skills in manual protocol probing
* Get hands on experience with (`curl`, `openssl`, `nc`, `telnet`, etc.)
* Provide a light intro to real-world obfuscation and protocol camouflage

## 🧪 How It Works

* Listens on **one external port** (default: `2345`)
* Peeks at the first few bytes sent by the client
* Matches against known protocol signatures
* Transparently reroutes the connection to a corresponding local service

Example:

* Client sends `SSH-2.0...` → gets routed to port `2222`
* Client sends `GET / HTTP/1.1` → routed to port `80`
* Client tries a TLS handshake → routed to port `443`

## 🔍 Why It Matters

In the real world:

* Attackers hide services on weird ports.
* Defenders use protocol obfuscation and deception.
* Automated scanners fail unless you get creative.

**SpectraGate** forces manual curiosity. There's no shortcut. No help. Just instinct.

> *Find the service in the signal. Not the number.*

## ⚙️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/SSHad0w/spectragate.git
   cd spectragate
   ```

2. (Optional) Review or modify `ROUTES` in `spectragate.py` to change the fingerprint mappings.

3. Run it:

   ```bash
   python3 spectragate.py --port 2345
   ```

4. On another machine, run `service_runner.sh`.

## 🧪 Test It Out

Try probing from a Kali VM or another machine:

```bash
curl http://your_ip:2345
nc your_ip 2345
openssl s_client -connect your_ip:2345
ssh -p 2345 your_ip
```

Didn’t work? Good. Debug it. That's the whole point.

## 🔐 Logs

Every successful connection is logged in `Spectragate.log`. Want to analyze behavior later? Check the timestamps and fingerprints.

## 🧱 Built With

* Python 3 (asyncio)
* A hunger for clarity
* A flair for the dramatic

## 🕳️ Hidden Portals

This project may evolve. Its architecture is a small fragment of a larger... spectrum.

Future plans may include:

* Simulated CTF challenges behind protocols
* Obfuscated protocol layers
* Response faking and deception traps
* Integration into broader lab environments

But today it’s just **SpectraGate**.

## 🖤 License

MIT. Learn from it. Modify it. Share it.
And remember: not everything behind the port is what it seems.

**See you on the other side of the SpectraGate.**
