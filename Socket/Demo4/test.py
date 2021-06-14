import socket
HOST = socket.gethostbyname(socket.gethostname())

if HOST == '127.0.1.1':
    print("GOOD")
print(HOST)