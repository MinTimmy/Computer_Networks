import socket
import time
import threading

HEADER = 64 # the message's byte can't higher then 64 bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#ADDR = (SERVER, PORT) #array has IP and pot
ADDR = ('', PORT) #array has IP and pot


FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #new a socket which is $over the internet by stream
server.bind(ADDR) # bound IP and port

def handle_client(conn, adder):
    print( "[NEW CONNECTION]" + str(adder) + "connected." )

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(HEADER.decode(FORMAT))

        if msg == DISCONNECT_MESSAGE:
            connected = False
        print("[" + str(adder) + "]" +  str(msg))
    # conn.sleep()
    conn.close()
def start():
    server.listen()
    print("[LISTENING] Server is listening on " + str(SERVER))
    while True:
        conn, adder = server.accept()
        thread = threading.Thread(target=handle_client(), args=(conn, adder))
        thread.start()
        print("[ACTIVE CONNECTIONS]" + str(threading.activeCount() - 1) )


print("[STARTING] server is starting...")
start()
