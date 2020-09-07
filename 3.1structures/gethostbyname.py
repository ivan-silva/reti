import socket
import sys

if len(sys.argv) < 2:
    name = "www.python.org"
else:
    [name] = sys.argv[1:]

print('Name is:', name)
try:
    host = socket.gethostbyname(name)
    print('Host', host)
except socket.gaierror as err:
    print("cannot resolve hostname: ", name, err)

