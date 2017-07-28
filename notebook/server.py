#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from notebook.socket_obj import BaseSocket
from notebook.socket_obj import ServerSocket
from notebook.controller import NoteService


class Server(object):
    """A Server object"""

    def __init__(self):
        """Initial a Server object"""
        self.controller = NoteService()
        self.socket_obj = ServerSocket()
        self.data = []
        self.choice = ""

        self.socket_obj.bind()
        client_socket, client_address = self.socket_obj.socket.accept()
        self.client_socket = BaseSocket(client_socket)
        print "[Client Address]", client_address

        self.main_func()

    def send_data(self, data):
        """Senf data ro server"""
        message = json.dumps(data, default=lambda obj: obj.__dict__,
                             indent=2)
        self.client_socket.send_message(message)

    def recive_data(self):
        """Recive data from server"""
        message = self.client_socket.recive_message()
        return json.loads(message) if message else None

    def main_func(self):
        arguements = self.recive_data()
        while arguements:
            self.choice, self.data = arguements
            self.send_data(self.exec_choice())
            arguements = self.recive_data()

    def exec_choice(self):
        print self.choice, self.data
        return_value = []
        if self.choice == 'ul':
            return_value = self.user_lognin()
        elif self.choice == 'ur':
            return_value = self.user_register()
        elif self.choice == 'q':
            return_value = self.exit_note()
        if self.choice == 'an':
            return_value = self.add_note()
        elif self.choice == 'dn':
            return_value = self.delete_note()
        elif self.choice == 'da':
            return_value = self.delete_all_note()
        elif self.choice == 'la':
            return_value = self.list_all_note()
        elif self.choice == 'lt':
            return_value = self.list_note_by_title()
        elif self.choice == 'lk':
            return_value = self.list_note_by_keyword()
        elif self.choice == 'et':
            return_value = self.update_note_title()
        elif self.choice == 'ec':
            return_value = self.update_note_content()
        return return_value

    def exit_note(self):
        """exit system"""
        self.controller.write_data()
        return True

    def user_lognin(self):
        """user login"""
        return self.controller.user_lognin(*self.data)

    def user_register(self):
        """user register"""
        return self.controller.create_user(*self.data)

    def add_note(self):
        """add note func"""
        return self.controller.create_note(*self.data)

    def delete_note(self):
        """delete note func"""
        return self.controller.delete_note(*self.data)

    def delete_all_note(self):
        """delete all note"""
        return self.controller.delete_all_note(*self.data)

    def list_all_note(self):
        """list all note"""
        return self.controller.list_all_note()

    def list_note_by_title(self):
        """"list all note by title"""
        return self.controller.querry_note_by_title(*self.data)

    def list_note_by_keyword(self):
        """list note by key word"""
        return self.controller.querry_note_by_keyword(*self.data)

    def update_note_title(self):
        """update note title"""
        return self.controller.update_note_title(*self.data)

    def update_note_content(self):
        """uodate note content"""
        return self.controller.update_note_data(*self.data)
