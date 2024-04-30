# Agent script

import socket

SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5151

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected to server")

while 1:
    print(s.recv(409600).decode())