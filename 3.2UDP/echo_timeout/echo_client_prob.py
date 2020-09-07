#!/usr/bin/env python

# Ivan Silva

import optparse
import signal
import sys
import time
from socket import *

parser = optparse.OptionParser()
parser.add_option('-s', '--server', dest="server", default="localhost", help="nome del server")
parser.add_option('-p', '--port', dest="port", type=int, default=25001, help="porta di ascolto del server")
parser.add_option('-t', '--timeout', dest="timeout", type=int, default=3, help="timeout per aspettare risposta")
parser.add_option('-m', '--message', dest="message", default="hello from Ivan Silva, in python",
                  help="messaggio  da spedire in risposta")
options, remainder = parser.parse_args()

print("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message)


def handler_alrm(signum, frame):
    print('Timeout. No reply')
    sys.exit(0)


def handler_int(signum, frame):
    print('Signal handler called with signal', signum)
    sys.exit(0)


# Set the signal handler and a 5-second alarm
# SIGALRM is not supported on Windows. https://docs.python.org/2/library/signal.html On Windows,
# signal() can only be called with
# SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, or SIGTERM.
# A ValueError will be raised in any other case
signal.signal(signal.SIGALRM, handler_alrm)
signal.signal(signal.SIGINT, handler_int)

addr = (options.server, options.port)
s = socket(AF_INET, SOCK_DGRAM)

ta = time.time()

Len = s.sendto(options.message.encode(), addr)
print("Message to: ", addr, " - data: ", options.message)

signal.alarm(options.timeout)
data, addr = s.recvfrom(1500)

print("Message from:", addr, "- data:", data)

tb = time.time()
print("Message tempo :", tb - ta)

s.close()
