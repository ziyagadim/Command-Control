import socket
import threading

def handle_client(conn):
    try:
        while True:
            command = input("Enter command to send to client (type 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            conn.sendall(command.encode())

            response = conn.recv(4096).decode()
            print("Response from client:", response)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def main():
    HOST = 'localhost'  # Change this to your server's IP address if needed
    PORT = 12345        # Change this to your desired port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()

if __name__ == "__main__":
    main()
