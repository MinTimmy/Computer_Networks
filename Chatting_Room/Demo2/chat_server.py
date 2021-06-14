# from Chatting_Room.Demo1.Clients import IP_address
# from Chatting_Room.Demo1.Server import IP_address
import socket
import select
from threading import *
import sys
import threading
import _thread
import threaded


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
# IP_address = "127.0.0.1"
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
                # print("It's: ",message.decode('UTF-8'))   
                if message:
                    print("<" + self.addr[0] + "> " + message)
                    message_to_send = "<" + self.addr[0] + "> " + message
                    self.broadcast(message_to_send,self.conn)
                    #prints the message and address of the user who just sent the message on the server terminal
                else:
                    self.remove(self.conn)
            except:
                continue
    
    def broadcast(self, message,connection):
        # print("Do broadcast")
        # print(list_of_clients)
        for clients in list_of_clients:
            if clients!=connection:
                try:
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

    print("hello")
    newtread = clientThread(clientAddress, clientSocket)
    newtread.start()

conn.close()
server.close()
