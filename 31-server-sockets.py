#!/usr/local/bin/python3
import socket

# Run at the same time as 31-client-sockets.py in a separate terminal
# Establish communication between server and client using TCP/IP
host = "localhost"
port = 4000

# Instantiate a socket using IPV4 and TCP/IP, these are the default values
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

# Number of connections to allow
sock.listen(1)
print("Lisenting for a connection on port: %i" % port)

# Returns a connection object and client address
client, addr = sock.accept()
print("Connected to: %s" % str(addr))
client.send("Hello, client.".encode())
client.send("Goodbye, client.".encode())

client.close()
