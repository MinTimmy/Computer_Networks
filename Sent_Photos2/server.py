import socket

from numpy import byte               # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '127.0.0.1'
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('311.jpg','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    print ("Receiving...")
    l = c.recv(2048)
    count = 0
    while (l):
        print ("Receiving..." + str(count))
        count += 1
        f.write(l)
        l = c.recv(2048)
    f.close()
    print ("Done Receiving")
    message = 'Thank you for connecting'
    c.send(bytes(message, 'UTF-8'))
    c.close()                # Close the connection