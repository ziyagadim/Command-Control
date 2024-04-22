from art import *
import socket
import threading
import pickle

def list():
    pass

def help():
    pass

def connect():
    with open('client_sockets.pkl', 'rb') as f:
        client_address = pickle.load(f)
    print(client_address)
    socket.socket().connect(client_address)
    socket.socket().send('salam'.encode())

def transfer():
    pass

def shell():
    pass

def listen_incoming():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()
        with open("client_sockets.pkl", "wb") as f:
            pickle.dump(client_socket.getpeername(), f)
        



threading.Thread(target=listen_incoming).start()


tprint("Server")

while 1:
    command = input("\n>")
    connect()
