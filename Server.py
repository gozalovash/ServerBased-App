import socket, argparse
import requests
from bs4 import BeautifulSoup

INTERFACE = '127.0.0.1'
PORT = 1060
BUFFSIZE = 4096
SEPARATOR = "@"
URL = "http://"

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
            print (webpage)
            result1, result2 = self.performCalculating(webpage)
            print('Sending result to the client ...')
            sc.send(f"{result1}{SEPARATOR}{result2}".encode())
            sc.close()
            print('Result sent, session closed!\n')

    def performCalculating(self, webpage):
        r = requests.get(URL+webpage)
        soup = BeautifulSoup(r.content, 'html5lib')
        images_count = len(soup.find_all('img'))
        p_list = soup.find_all('p')
        p_count = 0
        for p in p_list:
            if not p.find_all('p'):
                p_count += 1
        return images_count, p_count
