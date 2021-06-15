import socket
import select
from threading import *
import sys
import threading
import _thread
import threaded
import time


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket. This is used when we have an Internet Domain
with any two hosts
The second argument is the type of socket. SOCK_STREAM means that data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
IP_address = socket.gethostbyname(socket.gethostname())

Port = 8080
server.bind((IP_address, Port)) 


#listens for 100 active connections. This number can be increased as per convenience
list_of_clients=[]

class clientThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        threading.Thread.__init__(self)
        self.socket = clientSocket
        print("New Connection: " , self.addr[0])

    def run(self):
        print("Connection from", self.addr[0])
        CA = clientAddress
        message = ''
        
        while True:
            try:     
                message = self.conn.recv(2048).decode('UTF-8')
                print(message[:4]) 
                filename = message[5:len(message)-1]
                if message[:4] == "send":
                    file = open(filename,'wb')
                    temp = self.conn.recv(2048)
                    while temp != b'end\n':
                        file.write(temp)
                        temp = self.conn.recv(2048)
                    # self.broadcast_file(filename,self.conn)
                    print("The file is received successfully.")
                    file.close()
                else:
                    print(message)
                    print("<" + self.addr[0] + "> " + message)
                    message_to_send = "<" + self.addr[0] + "> " + message
                    self.broadcast_message(message_to_send,self.conn)
            except:
                self.remove(self.conn)
                continue
    def broadcast_file(self, filename, connection):
        print("Do broadcast")
        file = open("buffer", 'rb')
        print(list_of_clients)
        for clients in list_of_clients:
            if clients!=connection:
                print("hello1")
                clients.sendall(bytes('file', 'UTF-8'))
                print("hello2")
                time.sleep(2)
                clients.sendall(bytes('file', 'UTF-8'))
                print("hello3")
                time.sleep(1)
                try:
                    imgData = file.readline(2048)
                    print(imgData)
                    while(imgData):
                        clients.send(imgData)
                        imgData = file.readline(2048)
                        if not imgData:
                            break
                    time.sleep(5)
                    print("finish")
                    server.sendall(bytes('end\n', 'UTF-8'))
                except:
                    pass
                    # clients.close()
                    # self.remove(clients)

    def broadcast_message(self, message,connection):
        print("Do broadcast")
        print(list_of_clients)
        for clients in list_of_clients:
            if clients!=connection:
                try:
                    clients.sendall(bytes(message, 'UTF-8'))
                    time.sleep(2)
                    clients.sendall(bytes(message, 'UTF-8'))
                except:
                    clients.close()
                    self.remove(clients)

    def remove(self, connection):
        if connection in list_of_clients:
            list_of_clients.remove(connection)



while True:
    #binds the server to an entered IP address and at the specified port number. The client must be aware of these parameters
    server.listen(100)
    clientAddress, clientSocket = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    list_of_clients.append(clientAddress)
    # print(clientSocket[0] + " connected")
    print(clientSocket[0] + " connected")
    #maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    #Prints the address of the person who just connected
    # start_new_thread(clientthread,(conn,addr))
    #creates and individual thread for every user that connects
    # _thread.start_new_thread(clientthread,(conn,addr))

    # print("hello")
    # print(list_of_clients)
    newtread = clientThread(clientAddress, clientSocket)
    newtread.start()

conn.close()
server.close()
