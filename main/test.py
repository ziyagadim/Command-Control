import getpass
import platform

def get_info():
    

    os = platform.platform()
    hostname = platform.node()
    username = getpass.getuser()

    return {'os': os, 'hostname': hostname, 'username': username}


print(get_info['os'])