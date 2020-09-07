#!/usr/bin/env python

# Ivan Silva

from socket import *
import sys, time
import optparse

parser = optparse.OptionParser()
parser.add_option('-s', '--server', dest="server", default="127.0.0.1", help="nome del server (default localhost)")
parser.add_option('-p', '--port', dest="port", default=25000, type=int, help="porta di ascolto del server")
parser.add_option('-b', '--bufsize', dest="bufsize", default=100, type=int, help="dimensione buffer di spedizione")
options, remainder = parser.parse_args()
print("OPTIONS  server:", options.server, " - port:", options.port, " - bufsize:", options.bufsize)

addr = (options.server, options.port)
s = socket(AF_INET, SOCK_DGRAM)

ta = time.time()

Len = s.sendto("hello from Ivan Silva, in python".encode(), addr)
print("sent ", Len, " Bytes \n")

tb = time.time()
print("tempo :", tb - ta)

s.close()
