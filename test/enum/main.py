# import socket
# import platform
# import getpass

# print(socket.gethostname())
# print(platform.platform())
# print(getpass.getuser())



# a = {'salam':2}
# print(type(a))

# b = str(a)
# print(type(b))

# c = eval(b)
# print(type(c))

import socket,platform,getpass

def enumerate():
    hostname = socket.gethostname()
    OSver = platform.platform()
    username = getpass.getuser()

    return {'hostname':hostname, 'OS':OSver, 'username':username}