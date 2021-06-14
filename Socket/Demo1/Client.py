import socket

HEADER = 64 # the message's byte can't higher then 64 bytes
PORT = 6166
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
# SERVER = "192.168.3.139"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDER)