import socket

# Server configuration
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
path = "C:\\Users\\Student\\Desktop\\piton\\Command-Control\\file_transfer\\"
# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server is listening...")
    # Accept the connection
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # Receive the file name from the client
        file_name = conn.recv(1024).decode()
        file_name = path+file_name.split("\\")[-1]
        
        print("Receiving file:", file_name)
        # Open a new file with the received file name
        with open(file_name, 'ab') as file:
            # Receive the file data in chunks and write it to the file
            a = conn.recv(4096)
            while a != b"\n\r":
                file.write(a)
                a = conn.recv(4096)
            
        print("File received successfully!")
