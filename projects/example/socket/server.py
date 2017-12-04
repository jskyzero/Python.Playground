#!usr/bin/env python
# -*- coding: utf-8 -*-


import socket

# server config
HOST = ""
PORT = 9100


class ServerSocket(object):
    """A Server Socket Class"""

    def __init__(self):
        """Initial a ServerSocket object"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, host, port):
        """Bind to a host:port"""
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)

    def start_socket(self):
        """Start a socket server"""
        self.show_local_ip()
        self.bind(HOST, PORT)
        client_socket, client_address = self.server_socket.accept()
        print "Connerted by", client_address
        # begin recive data
        filename = client_socket.recv(1024)
        self.recive_file(filename, client_socket)

    def recive_file(self, filename, client_socket):
        """receive file from client_socket"""
        with open(filename, 'w') as save_file:
            while True:
                file_piece = client_socket.recv(1024)
                if file_piece:
                    save_file.write(file_piece)
                else:
                    break
            client_socket.close()

    def show_local_ip(self):
        """Show local ip"""
        print "[Server Starting]"
        print "[Local IP]", self.get_local_ip()

    def get_local_ip(self):
        """Return local ip address"""
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("gmail.com", 80))
        localip = temp_socket.getsockname()[0]
        temp_socket.close()
        return localip

if __name__ == "__main__":
    SERVER = ServerSocket()
    SERVER.start_socket()
