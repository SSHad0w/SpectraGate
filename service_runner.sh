bash -c 'while true; do echo -e "SSH-2.0-OpenSSH_8.9p1 Debian-4" | nc -nlvp 2222; done' & \
bash -c 'while true; do echo -e "HTTP/1.1 200 OK\nServer: Apache/2.4.41 (Ubuntu)\n\n<html><h1>Welcome, Hacker.</h1></html>" | nc -nlvp 80; done' & \
bash -c 'while true; do echo -e "220 Microsoft FTP Service\n" | nc -nlvp 21; done' & \
bash -c 'while true; do echo -ne "\x16\x03\x01\x00\x2a\x01\x00\x00\x26\x03\x03" | nc -nlvp 443; done' & \
bash -c 'while true; do echo -e "\xff\xfd\x18\xff\xfd\x20\r\nLogin: " | nc -nlvp 23; done'

