# com&conTROLL
com&conTROLL is basic C2 server for multiple clients.

## Installation
1.First download project as zip from https://github.com/ziyagadim/Command-Control.git
2.Unzip package and open path in cmd
3.
```bash
pip install -r requirements.txt
```
4.It is ready for run
```bash
python server.py
```
5.For client repeat steps 3 and 4

## Usage
Server side commands:
```bash
list    Lists all connected client
use     Interracting specified client Usage: use <ID number>
help    shows help page
```
Client interraction capabilities:
```bash
download    Downloads file from client to server. Usage: download <path of file want to download> <path where you want to save>
upload      Uploads file from seerver to client. Usage: upload <path of file want to upload> <client side path where you want to save>
shell       Opens reverse shell in target machine
ss          Takes screenshoot of target machine and sends it to server
exit        Exiting from current client's session 
```

## Things you need to know
• screenshoot function can make error for screen size problems
• Change IP address and port on both server and client code into yours.
• Change download path on server.py script into yours. (line 41)