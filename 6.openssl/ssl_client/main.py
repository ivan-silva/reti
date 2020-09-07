import socket
import ssl


def ssl_connect(url: str, cert_path: str, port=443):
    simple_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ssl_sock = ssl.wrap_socket(sock,
    #                            ca_certs='./cacert.pem',  # concatenated “certification authority” certificates
    #                            cert_reqs=ssl.CERT_REQUIRED)  # cert is required from other side
    # ssl_sock.connect(('netlab.fis.unipr.it', 443))
    ssl_sock = ssl.wrap_socket(simple_sock,
                               ca_certs=cert_path,  # concatenated “certification authority” certificates)
                               cert_reqs=ssl.CERT_REQUIRED)  # cert is required from other side
    ssl_sock.connect((url, port))
    return ssl_sock


if __name__ == "__main__":

    # Crea un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connette il socket alla porta sulla quale il server e' in ascolto
    server_address = ('localhost', 13337)
    print('Mi connetto al server %s sulla porta %s' % server_address)
    sock.connect(server_address)

    try:

        message = "Sempre caro mi fu quest'ermo colle, e questa siepe, che da tanta parte dell'ultimo orizzonte il guardo esclude."

        print('Invio il messaggio', message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        header = "$" + str(amount_expected) + "$"
        sock.sendall(header.encode())
        sock.sendall(message.encode())

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('Ricevuto:', data.decode())

    finally:
        print('closing socket')
        sock.close()
