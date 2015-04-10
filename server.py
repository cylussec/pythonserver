#!/usr/bin/python3

import socket
import csv
import argparse
import signal
import sys
import select
from multiprocessing.connection import Listener
from array import array
from threading import Thread

def handler(signum, frame):
    print("Closing")
    del(cls)

class ExponentServer:
    def __init__(self, port, password_file, host=None):
        self.port = port
        self.password_dict = {}
        self.host=host

        # Parse the CSV file
        with open(password_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            for row in reader:
                self.password_dict[row[0]] = row[1]

class ThreadedExponentServer(ExponentServer):
    def __init__(self, port, password_file, host='localhost'):
        super(ThreadedExponentServer, self).__init__(port, password_file, host)

    def start(self):
        # Use multiprocessing to handle our server
        with Listener((self.host, self.port)) as self.listener:
            while True:
                conn = self.listener.accept()
                t = Thread(target=self._process_connection, args=(conn,))
                t.daemon = True
                t.start()

    def _process_connection(self, conn):
        """
            Works with our threaded connection to handle connections
        """
        print('connection accepted from', self.listener.last_accepted)
        password = conn.recv()
        try:
            const_value = self.password_dict[password]
            print("Got password {}".format(password))
            conn.send("AUTH")
        except KeyError:
            print("Got invalid password {}".format(password))
            conn.send("NOAUTH")
            return None


        while True:
            try:
                try:
                    value = conn.recv()
                except OSError:
                    break 

                if not value:
                    break

                calc_value = int(value)**int(const_value)

                print("Received {}; Sending {}".format(value, calc_value))

                conn.send(calc_value)
            except EOFError:
                print("Connection closing")
                conn.close()


class NonThreadedExponentServer(ExponentServer):
    def __init__(self, port, password_file, host=None):
        super(NonThreadedExponentServer, self).__init__(port, password_file, host)

        # Setup the server
        for res in socket.getaddrinfo(self.host, self.port, socket.AF_UNSPEC,
                                      socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            af, socktype, proto, canonname, sa = res
            try:
                self.s = socket.socket(af, socktype, proto)
            except OSError as msg:
                self.s = None
                continue
            try:
                self.s.bind(sa)
                self.s.listen(1)
            except OSError as msg:
                self.s.close()
                self.s = None
                continue
            break
        if self.s is None:
            raise RuntimeError('could not open socket')

    def start(self):
        while True:
            conn, ip = self.s.accept()
            password = conn.recv(1024).decode('utf-8')
            try:
                const_value = self.password_dict[password]
                print("Got password {}".format(password))
                conn.send("AUTH".encode('utf-8'))
            except KeyError:
                print("Got invalid password {}".format(password))
                conn.send("NOAUTH".encode('utf-8'))
                break

            while True:
                try:
                    value = conn.recv(1024).decode('utf-8')
                except ConnectionResetError:
                    break

                if not value: 
                    break

                calc_value = int(value)**int(const_value)

                print("Received {}; Sending {}".format(value, calc_value))
                
                #You said you wanted big
                conn.send(calc_value.to_bytes(2048, byteorder='little'))
            conn.close()
        self.s.shutdown(SHUT_RD)
        self.s.close()


signal.signal(signal.SIGINT, handler)

# Arguments
parser = argparse.ArgumentParser(description="Start integer processing server")
parser.add_argument('-p', '--port', type=int, help="port the server should "
    "listen on", required=True)
parser.add_argument('-f', '--csvfile', help="path to the csv password file",
    required=True)
parser.add_argument('-t', '--threaded', action='store_true', help='Use the '
    'threaded version of the server. Default: False')
args = parser.parse_args()

if args.threaded:
    cls = ThreadedExponentServer
else:
    cls = NonThreadedExponentServer

cls = cls(args.port, args.csvfile)
cls.start()
