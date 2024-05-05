import socket,time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)

print("LISTENING...")

client_socket, address = server_socket.accept()

print("GOT CONENCTION!!!")

file_name ="ss" + time.ctime().split()[3].replace(':', '-') + '.png'

file = open(file_name, 'ab')
a = client_socket.recv(4096)

while a != b'\n\r':
    file.write(a)
    a = client_socket.recv(4096)
file.close()

print("FILE RECIEVED SUCCESSFULLY!!!")
