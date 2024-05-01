import socket,time

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Get the file path from the user
file_path = input("Enter the file path to transfer: ")

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    # Send the file name to the server
    s.send(file_path.encode())
    # Open the file to be sent
    time.sleep(0.3)
    with open(file_path, 'rb') as file:
        # Read the file data in chunks and send it to the server
        a = file.read(4096)
        while a:
            s.send(a)
            a = file.read(4096)
        
        s.send(b"\n\r")
    print("File sent successfully!")
