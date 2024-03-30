#create a TCP socket (SOCK_STREAM)
import socket
from time import ctime

HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    while True:
        print('Server waiting for connection...')
        client, addr = server.accept()
        print('Client connected from: {addr}')

        while True:
            data = client.recv(BUFSIZ)
            if not data or data.decode('utf-8') == 'END':
                break
            print(f'Received from client: {data.decode("utf- 8")}')
            print(f'Sending the server time to client: {ctime()}')
            try:
                client.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print('Connection closed by client')
        client.close()
        break
