import socket
import threading

class clientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.socket = clientSocket
        print("New Connection: " , clientAddress)

    def run(self):
        print("Connection from", clientAddress)
        CA = clientAddress
        message = ''
        while True:
            data = self.socket.recv(256)
            message = data.decode()
            if message == 'exit':
                break
            print("From client " , CA, ": ", message)
            self.socket.send(bytes(message, 'UTF-8'))
        print("Client ", CA, "disconnected.")




HOST = socket.gethostbyname(socket.gethostname())
#HOST = '127.0.0.1'
PORT = 8080


# create a raw socket and bind it to the public interface
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.bind((HOST, PORT))
server.bind(('',PORT))

# Include IP headers avoid two clients connect to the server at the same time
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# receive all packages
# server.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)




print("Server is on")
print("Server is waiting for connection... ")

while True:
    server.listen(1)
    clientSocket , clientAddress = server.accept()
    newtread = clientThread(clientAddress, clientSocket)
    newtread.start()





