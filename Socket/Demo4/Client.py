import socket
import sys
SERVER_HOST = '192.168.3.139'
#SERVER_HOST = '127.0.0.1'
#SERVER_HOST = socket.gethostbyname(socket.gethostname())

PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, PORT))

message = input("Type your message (Type 'exit' to close): ")
client.sendall(bytes(message, 'UTF-8'))

if message == 'exit':
    print("The client leave...")
    client.close()
    sys.exit()

check = True
while check:
    in_data = client.recv(256)
    print("From server: ", in_data.decode())
    print("------------------------------------------")
    message = input("Please type new message: (type 'exit' to close)")
    if message == 'exit':
        check = False
    client.sendall(bytes(message, 'UTF-8'))
    


print("The client leave...")
client.close()
sys.exit()

client.close()