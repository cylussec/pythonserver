#!/usr/bin/python3

import argparse
import socket
import sys
import signal
import time
from multiprocessing.connection import Client

def handler(signum, frame):
    print("Closing")
    sys.exit(0)

class ExponentClient:
    def __init__(self, ip, port, password):
        self.ip = ip
        self.port = port
        self.password = password

    def start(self):
        while True:
            value = input("Enter value: ")
            if not value:
                break
            print("Received: {}".format(int(self.send(value))))


class ThreadedExponentClient(ExponentClient):
    def __init__(self, ip, port, password):
        super(ThreadedExponentClient, self).__init__(ip, port, password)

        self.conn = Client((self.ip, self.port))
        self.conn.send(args.password)
        auth_value = self.conn.recv()

        if auth_value == 'AUTH':
            print("Authorized")
        else:
            raise RuntimeError("Invalid Password")

    def __del__(self):
        self.conn.close()


    def send(self, value):
        self.conn.send(value)
        return self.conn.recv()

class NonThreadedExponentClient(ExponentClient):
    def __init__(self, ip, port, password):
        super(NonThreadedExponentClient, self).__init__(ip, port, password)
        
        self.s = None
        for res in socket.getaddrinfo(self.ip, self.port, socket.AF_UNSPEC, 
            socket.SOCK_STREAM):
            
            af, socktype, proto, canonname, sa = res
            try:
                self.s = socket.socket(af, socktype, proto)
            except OSError as msg:
                self.s = None
                continue
            try:
                self.s.connect(sa)
            except OSError as msg:
                self.s.close()
                self.s = None
                continue
            break
        if self.s is None:
            print('could not open socket')
            sys.exit(1)
        self.s.send(bytes(args.password, 'utf-8'))
        auth_value = self.s.recv(1024).decode('utf-8')

        if auth_value == 'AUTH':
            print("Authorized")
        else:
            raise RuntimeError("Invalid Password")

    def __del__(self):
        if self.s:
            self.s.close()

    def send(self, value):
        self.s.send(bytes(value, 'utf-8'))
        return int.from_bytes(self.s.recv(2048), byteorder='little')

parser = argparse.ArgumentParser(description="Connect to integer processing"
    " server")
parser.add_argument('-s', '--server', help="Server IP in dotted decimal "
    "notation", required=True)
parser.add_argument('-p', '--port', type=int, help="port the server should "
    "listen on", required=True)
parser.add_argument('-t', '--threaded', action='store_true', help='Use the '
    'threaded version of the server. Default: False')
parser.add_argument('-a', '--password', required=True)
args = parser.parse_args()

signal.signal(signal.SIGINT, handler)

if args.threaded:
    cls = ThreadedExponentClient
else:
    cls = NonThreadedExponentClient

cls = cls(args.server, args.port, args.password)
cls.start()
 