import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

str1 = input("Please input something for server: ")


#print(str1)

tmp = bytes(str1, encoding='ascii')


while True:
    s.sendto(tmp, ('127.0.0.1', 8888))
    print(s.recv(1024))
    if str1 == 'exit':
        break
    str1 = input("Please input something for server again: ")
    tmp = bytes(str1, encoding='ascii')

"""
for data in [b'dog']:
    print(data)
    print('\n')
    #s.sendto(data, ('127.0.0.1', 8888))
    #print(s.recv(1024))
"""
s.close()
