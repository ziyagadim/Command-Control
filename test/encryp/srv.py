from art import *
import socket
import threading
import sys
import time
from prettytable import PrettyTable

from Crypto.Cipher import AES

key = b'ZiyaGadimli12345'
nonce = b'ZiyaGadimli54321'

ciper = AES.new(key, AES.MODE_EAX, nonce)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = server_socket.accept()

def download(from_, where):
    # client_socket.recv(4096)
    client_socket.send(from_.encode())
    time.sleep(0.3)
    file_name = from_.split('\\')[-1]
    if not where.endswith('\\'):
        where += '\\'
    where += file_name
    file = open(where, 'ab')
    a = client_socket.recv(4096)
    a = ciper.decrypt(a)

    num = 0 #TODO delete
    while a != b"\n\r":
        file.write(a)
        a = client_socket.recv(4096)
        print(f"CHUNK {num} RECIEVED ") #TODO delete
        a = ciper.decrypt(a)
        print(f"CHUNK {num} DECRYPTED") #TODO delete
        num += 1 #TODO delete
    file.close()
    print("File sent succesfully!")


download(r'C:\Windows\Temp\salam.txt' ,r'C:\Windows\Temp\salam')
