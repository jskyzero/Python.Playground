#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

# socker config
HOST = ""
PORT = 9110
EACH_MESSAGE_LENGTH = 2
MESSAGE_LENGTN_FORMAT = ">I"
NET_WORK_BYTE = 4


class BaseSocket(object):
    """A base Socket class"""

    def __init__(self, use_socket=None):
        """Initial a socket class"""
        self.socket = use_socket if use_socket else socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        """Close a socket"""
        self.socket.close()

    def get_local_ip(self):
        """Return local ip address"""
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("gmail.com", 80))
        localip = temp_socket.getsockname()[0]
        temp_socket.close()
        return localip

    def recive_message(self):
        """Recive message from """
        message_length = self.recive_all(NET_WORK_BYTE)
        if not message_length:
            return None
        message_length = struct.unpack(
            MESSAGE_LENGTN_FORMAT, message_length)[0]
        return self.recive_all(message_length)

    def recive_all(self, message_length):
        """Recive message_length byte or return None if EOF is hit"""
        data = ""
        while len(data) < message_length:
            packet = self.socket.recv(
                min(message_length - len(data), EACH_MESSAGE_LENGTH))
            if not packet:
                return None
            data += packet
        return data

    def send_message(self, message):
        """send message to server"""
        # Prefix each message with a 4-byte length (network byte order)
        message = struct.pack(MESSAGE_LENGTN_FORMAT, len(message)) + message
        self.socket.sendall(message)


class ServerSocket(BaseSocket):
    """A Server Socket"""

    def bind(self, host="", port=PORT):
        """Bind to a host:port"""
        self.socket.bind((host, port))
        self.socket.listen(1)

    def start_socket(self):
        """Start a socket server"""
        self.show_local_ip()
        self.bind(HOST, PORT)
        client_socket, client_address = self.socket.accept()

        client_socket = BaseSocket(client_socket)
        print "Connerted by", client_address
        recive_massage = client_socket.recive_message()
        while recive_massage:
            print "[Recv]", recive_massage
            client_socket.send_message(recive_massage[::2])
            recive_massage = client_socket.recive_message()
        self.close()

    def show_local_ip(self):
        """Show local ip"""
        print "[Server Starting]"
        print "[Local IP]", self.get_local_ip()


class ClientSocket(BaseSocket):
    """A Client socket Class"""

    def connect(self, host=HOST, port=PORT):
        """Connect to a Server"""
        self.socket.connect((host, port))

    def ask_send_ip(self):
        """Ask server ip address ans return"""
        server_ip = raw_input("[Server IP] ")
        return server_ip

    def start_socket(self):
        """Start a socket client"""
        message = raw_input("[message] ")
        while message:
            self.send_message(message)
            print "[BACK] ", self.recive_message()
            message = raw_input("[message] ")
        self.close()

if __name__ == "__main__":
    SOCKET = BaseSocket()
    print "[Local IP Adress]", SOCKET.get_local_ip()
