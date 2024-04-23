from art import *
import socket
import threading
import sys

connections = []

def list():
    for connection in connections:
        print(connection)

def help():
    pass



def transfer():
    pass

def shell(connection):
    print(connections[int(input) - 1]['address'])
    print(type(connections[int(input) - 1]['address']))
    # server_socket.connect(connections[int(input) - 1]['address'])
    pass

def exit():
    server_socket.close()
    sys.exit()


def listen_incoming():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5151

    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Listen for incoming connections
    server_socket.listen(5)
    # print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()
        connection = {"address": address, 'socket': client_socket}
        connections.append(connection)
        
        

tprint("Server")
threading.Thread(target=listen_incoming).start()

while 1:
    command = input("\n[*] Enter command > ")
    
    command = command.split(" ")

    match command[0]:
        case "list":
            list()
        case "help":
            help()
        case "transfer":
            transfer()
        case "shell":
            shell(command[1])
        case 'exit':
            exit()