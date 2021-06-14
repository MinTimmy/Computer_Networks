import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '127.0.0.1'
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
message = "Hello server"
# s.send(bytes(message, 'UTF-8'))
f = open('test1.mp4','rb')
print( 'Sending...')
imgData = f.readline(2048)
# l = f.read(1024)
# s.send(imgData)
count = 0
while (imgData):
    print(count)
    count += 1
    s.send(imgData)
    imgData = f.readline(2048)
    if not imgData:
        break
    
f.close()

print ("Done Sending")
# print (s.recv(1024))
# s.close                     # Close the socket when done
s.shutdown(socket.SHUT_WR)