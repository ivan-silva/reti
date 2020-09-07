# Ivan Silva


import optparse
import signal
import sys
from random import randint
from socket import *

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest="port", default=25000, type=int)
parser.add_option('-s', '--server', dest="server", default="0.0.0.0", )
parser.add_option('-b', '--bufsize', dest="bufsize", default=1024, type=int, help="dimensione buffer")
parser.add_option('-r', '--probability', dest="prob", default=50, type=int)
options, remainder = parser.parse_args()

print("   port:", options.port, "  server:", options.server, "bufsize:", options.bufsize)


def handler_int(signum, frame):
    print('Signal handler called with signal', signum)
    sys.exit(0)


signal.signal(signal.SIGINT, handler_int)

s = socket(AF_INET, SOCK_DGRAM)
s.bind((options.server, options.port))

sSend = socket(AF_INET, SOCK_DGRAM)

while 1:
    data, addr = s.recvfrom(options.bufsize)
    print("addr:", addr, " data:", data)
    if randint(1, 100) < options.prob:
        sSend.sendto(data, (addr[0], addr[1]))
        print("Answering...")
    else:
        print("Not answering...")
