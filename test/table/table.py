from prettytable import PrettyTable

list = [{'address': ('127.0.0.1', 54996), 'socket': 'socket', 'cred': 
         {'hostname': 'ACC-DT-DE-JM40', 'OS': 'Windows-11-10.0.22631-SP0', 'username': 'Student'}}, {'address': ('127.0.0.1', 33333), 'socket': 'socket', 'cred': 
         {'hostname': 'ACC-DT-DE-JM41', 'OS': 'Windows-11-10.0.22631-SP0', 'username': 'Student'}}]

table = PrettyTable(["ID", "IP", "port", 'Hostname', 'OS', 'Username'])

for i in range(len(list)):
    table.add_row([i,list[i]['address'][0],list[i]['address'][1],list[i]['cred']['hostname'],
                  list[i]['cred']['OS'],list[i]['cred']['username']])

print(table)

