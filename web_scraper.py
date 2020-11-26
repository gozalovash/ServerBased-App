import socket, argparse
from  Server import Server

INTERFACE = '127.0.0.1'
PORT = 1060
BUFFSIZE = 4096
SEPARATOR = "@"

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self, webpage):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        print('Client has been assigned socket name:', sock.getsockname())
        print('Sending webpage...')
        sock.send(f"{webpage}".encode())

        print('Receiving reply from server...')
        received = sock.recv(BUFFSIZE).decode()
        result1, result2 = received.split(SEPARATOR)
        print(f'Image count: {result1}, <p> leafs count: {result2}')
        sock.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['client', 'server'])
    parser.add_argument('-p', metavar="web page")
    args = parser.parse_args()

    if args.mode == 'server':
        Server(INTERFACE, PORT).bind()

    elif args.mode == 'client' and not args.p:
        parser.error('-p argument is required for "client" mode')
    else:
        Client(INTERFACE, PORT).connect(args.p)


if __name__ == '__main__':
    main()