import socket               # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '127.0.0.1'
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
message = "Hello server"
s.send(bytes(message, 'UTF-8'))
f = open('2.jpg','rb')
print( 'Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()

print ("Done Sending")
# print (s.recv(1024))
# s.close                     # Close the socket when done
s.shutdown(socket.SHUT_WR)