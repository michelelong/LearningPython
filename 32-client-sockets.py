#!/usr/local/bin/python3
import socket

host = "localhost"
port = 4000

sock = socket.socket()
sock.connect((host, port))

# Buffer size
msg = sock.recv(1024)

while msg:
    print("Received: %s" % msg.decode())
    msg = sock.recv(1024)

sock.close()
