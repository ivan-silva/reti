import socket
name = "www.fis.unipr.it"
result = socket.getaddrinfo(name, None, 0, socket.SOCK_STREAM)

print('Name is:', name)

for item in result:
    print(item)
    print('Address is:', item[4][0])

