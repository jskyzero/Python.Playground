#!usr/bin/env python
# -*- coding: utf-8 -*-


import socket

# server config
HOST = ""
PORT = 9100


class ClientSocket(object):
    """A Client socket Class"""

    def __init__(self):
        """Initial a ClientSocket object"""
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        """Connect to a Server"""
        self.client_socket.connect((host, port))

    def start_socket(self):
        """Start a socket client"""
        server_ip = self.ask_sent_ip()
        self.connect(server_ip, PORT)
        file_adress = self.ask_file_adress()
        self.sent_file(file_adress)

    def ask_sent_ip(self):
        """Ask server ip address ans return"""
        server_ip = raw_input("[Server IP] ")
        return server_ip

    def ask_file_adress(self):
        """Ask file adress and return"""
        file_address = raw_input("[File Address] ")
        return file_address

    def sent_file(self, file_adress):
        """sent file content to server"""
        self.client_socket.sendall(file_adress.split('/')[-1])
        with open(file_adress, 'r') as read_file:
            file_piece = read_file.read(1024)
            while file_piece:
                self.client_socket.sendall(file_piece)
                file_piece = read_file.read(1024)
            self.client_socket.close()

if __name__ == "__main__":
    CLIENT = ClientSocket()
    CLIENT.start_socket()
