# Ivan Silva
# 11 Dicembre 2014

import optparse
import signal
import sys
from socket import *
from threading import Thread

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest="port", default=25001, type=int)
parser.add_option('-b', '--bufsize', dest="bufsize", default=1024, type=int, help="dimensione buffer")
parser.add_option('-l', '--logfile', dest="logfilename", default="log.txt")
options, remainder = parser.parse_args()


def listener(sock):
    while (1):
        data, addr = sock.recvfrom(options.bufsize)
        print("Address ", addr[0], " sent from port ", addr[1], " the following message: ", data.decode())
        logfile.write(
            "Address " + addr[0] + " sent from port " + str(addr[1]) + " the following message: " + data.decode() + "\n")


def sigintHandler(signum, frame):
    print('Signal handler called with signal ', signum)
    logfile.close()
    sys.exit()


sockRec = socket(AF_INET, SOCK_DGRAM)
sockRec.bind(('0.0.0.0', options.port))
print("Listening on port ", options.port)

sockSend = socket(AF_INET, SOCK_DGRAM)

logfile = open(options.logfilename, "a")

listenerThread = Thread(target=listener, args=(sockRec,))
listenerThread.setDaemon(True)
listenerThread.start()

signal.signal(signal.SIGINT, sigintHandler)

while (1):
    hname = input("Hostname> ")
    if hname.strip() == "": continue
    while (1):
        port = input("Port> ")
        if port.strip() == "": continue
        try:
            port = int(port)
            break
        except ValueError:
            print("Invalid port")
    message = input("Message> ")
    if message.strip() == "": continue
    try:
        sockSend.sendto(message.encode(), (hname, port))
        print("Sent to address " + hname + " and port " + str(port) + " the following message: " + message + "\n")
        logfile.write(
            "Sent to address " + hname + " and port " + str(port) + " the following message: " + message + "\n")
    except:
        print("Unable to send message")
        logfile.write("Failed to send to address " + hname + " and port " + str(
            port) + " the following message: " + message + "\n")
