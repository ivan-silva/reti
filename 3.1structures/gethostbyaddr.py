import socket
import sys

if len(sys.argv) < 2:
    addr = "8.8.8.8"
else:
    [addr] = sys.argv[1:]

print('Addr is:', addr)
try:
    host, aliases, ip_addresses = socket.gethostbyaddr(addr)
    print('Host', host)
    print('Aliases', aliases)
    print('IP addresses', ip_addresses)
except socket.gaierror as err:
    print("cannot resolve hostname: ", addr, err)

