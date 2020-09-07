import socket
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind del socket alla porta
server_address = ('localhost', 13337)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Mi metto in ascolto di eventuali connessioni
sock.listen(1)

while True:

    print('In attesa di connessioni...')
    connection, client_address = sock.accept()

    try:
        print('Connessione in arrivo da', client_address)

        # Decido la dimensione del buffer
        BUF_SIZE = 32
        message = ""
        length = 0
        remaining_chars = 0

        while True:
            # Mi metto in ascolto, bloccante
            data = connection.recv(BUF_SIZE)
            decoded_data = data.decode()
            print('Pacchetto ricevuto: ', decoded_data)
            message_chunk = decoded_data
            # Se trovo l'intestazione contenente la lunghezza del messaggio
            # salvo la lunghezza e rimuovo l'header
            tokens = re.findall(r'\$(.*?)\$', decoded_data)
            if len(tokens) > 0:
                length = tokens[0]
                message_chunk = decoded_data.replace('$' + length + '$', '')
                remaining_chars = int(length)
                print('Trovata intestazione, in attesa di un messaggio di lunghezza ', remaining_chars)

            print('Caratteri rimanenti:', remaining_chars)
            if data:
                if remaining_chars > 0:
                    message += message_chunk
                    if (len(decoded_data) < BUF_SIZE) | (remaining_chars == BUF_SIZE):
                        print('EOF', client_address)
                        print('Reinvio messaggio completo:', message)
                        connection.sendall(message.encode())
                    remaining_chars -= len(message_chunk)
            else:
                print('Trasmissione dal client conclusa', client_address)
                connection.close()
                break

    finally:
        # Clean up the connection
        connection.close()
