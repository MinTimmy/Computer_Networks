# from Chatting_Room.Demo1.Server import IP_address
import socket
import select
import sys
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

# IP_address = "127.0.0.1"
# IP_address = "192.168.0.128"
# IP_address = '172.20.10.6'
Port = 8080

server.connect((IP_address, Port))

while True:
    print("Connecting successfully")
    sockets_list = [sys.stdin, server]
    print("hello1")
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    print("hello2", read_sockets)
    for socks in read_sockets:
        if socks == server:
            print("------------------------\nReceive\n-----------------------------")
            message = socks.recv(2048).decode('UTF-8')
            if message == "file":
                file = open(message, 'wb')
                message = ""
                message = socks.recv(2048)
                while message != b'end\n':
                    file.write(message)
                    message = socks.recv(2048)
            else:
                message = ""
                message = socks.recv(2048).decode('UTF-8')
                print (message)
            print("------------------------\nFinish Receive\n-----------------------------")
        else:
            print("------------------------\nSend\n-----------------------------")
            message = sys.stdin.readline()
            # print("[" + socket.gethostbyname(socket.gethostname()) + "] ", end='')
            # print(message)
            if message[0:4] == "send":
                message = 'send 2.jpg\n'
                server.sendall(bytes(message, 'UTF-8'))
                time.sleep(1)
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
                file = open(message[5:len(message)-1], 'rb')
                imgData = file.readline(2048)
                print("sending....")
                while(imgData): 
                    server.send(imgData)
                    imgData = file.readline(2048)
                    if not imgData:
                        break
                time.sleep(5)
                print("finish")
                server.sendall(bytes('end\n', 'UTF-8'))
            else: 
                server.sendall(bytes(message, 'UTF-8'))
                if message == 'leave':
                    server.close()
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
            print("------------------------\nfinish Send\n-----------------------------")
            
               
            
server.close()