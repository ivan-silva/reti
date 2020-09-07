#!/usr/bin/env python

# Nome Cognome - Data - versione
# Il receiver riceve una prima riga con il nome del file da scrivere
# poi riceve i dati che scrive sul file

import optparse
from socket import *

parser = optparse.OptionParser()
parser.add_option('-t', '--timeout', dest="timeout", default=1024, )
parser.add_option('-p', '--port', dest="port", default=9999, type=int)
parser.add_option('-b', '--bufsize', dest="bufsize", default=100, help="dimensione buffer di spedizione")

options, remainder = parser.parse_args()

print("Port:", options.port)

host = "0.0.0.0"
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, options.port))

addr = (host, options.port)

data, addr = s.recvfrom(options.bufsize)
filename = data.strip('\0'.encode())
print("file:", filename)

fout = open(filename, 'wb')

i = 1
data, addr = s.recvfrom(options.bufsize)
print("data:", data)
try:
    while (data):
        print("receiving ", i, "numbytes: ", len(data), " from: ", addr)
        i = i + 1
        fout.write(data)
        s.settimeout(options.timeout)
        data, addr = s.recvfrom(options.bufsize)
except timeout:
    fout.close()
    s.close()

print("File ", filename, "  received")
