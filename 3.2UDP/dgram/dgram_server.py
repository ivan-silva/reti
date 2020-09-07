#!/usr/bin/env python

# Ivan Silva


# import select
import optparse
import signal
import sys
from socket import *

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest="port", default=25000, type=int)
parser.add_option('-s', '--server', dest="server", default="127.0.0.1", )
parser.add_option('-b', '--bufsize', dest="bufsize", default=1024, type=int, help="dimensione buffer")
options, remainder = parser.parse_args()

print("   port:", options.port, "  server:", options.server, "bufsize:", options.bufsize)


def handler_alrm(signum, frame):
    print('Signal handler called with signal', signum)
    signal.alarm(options.timeout)
    global N
    N = 0


def handler_int(signum, frame):
    print('Signal handler called with signal', signum)
    sys.exit(0)


# signal.signal(signal.SIGALRM, handler_alrm)
signal.signal(signal.SIGINT, handler_int)

s = socket(AF_INET, SOCK_DGRAM)
s.bind((options.server, options.port))

while (1):
    data, addr = s.recvfrom(options.bufsize)
    print("addr:", addr, " data:", data.decode())
