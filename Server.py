import socket, argparse

INTERFACE = '127.0.0.1'
PORT = 1060
BUFFSIZE = 4096
SEPARATOR = "@"

class Server:
    def __init__(self, interface, port):
        self.interface = interface
        self.port = port

    def bind(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.interface, self.port))
        sock.listen(1)
        print(f'Listening at: {sock.getsockname()}')

        while True:
            sc, sockname = sock.accept()
            print("Accepted connection from ", sockname)
            print('Receiving web Page: ')
            webpage = sc.recv(BUFFSIZE).decode()
            result1, result2 = self.performCalculating(webpage)
            print('Sending result to the client ...')
            sc.send(f"{result1}{SEPARATOR}{result2}".encode())
            sc.close()
            print('Result sent, session closed!\n')

    def performCalculating(self, webpage):
        return 1, 2