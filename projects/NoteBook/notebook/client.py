#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hashlib
from notebook.socket_obj import ClientSocket


class Client(object):
    """A Client object"""

    def __init__(self):
        """Initial a Client object"""
        self.socket_obj = ClientSocket()
        self.socket_obj.connect()
        self.choice = ""
        self.user = ""
        self.user_func()

    def remove_controller(self, *data):
        """Send message to server and recive message from server"""
        self.send_data(data)
        return self.recive_data()

    def send_data(self, data):
        """Senf data ro server"""
        message = json.dumps((self.choice, data))
        self.socket_obj.send_message(message)

    def recive_data(self):
        """Recive data from server"""
        message = self.socket_obj.recive_message()
        return json.loads(message) if message else None

    def exit_note(self):
        """exit system"""
        self.user = ""
        if self.remove_controller():
            self.socket_obj.close()
            return True

    def user_func(self):
        """user system"""
        user_menu = (
            ('ul', 'user login in '),
            ('ur', 'user register'),
            ('q', 'quit system')
        )
        while self.choice != 'q':
            self.show_menu(user_menu)
            self.choice = raw_input("NoteBook $ ")
            self.exec_choice_user(user_menu)
            if self.user:
                self.main_func()

    def exec_choice_user(self, user_menu):
        """exec the choice"""
        func_return = self.show_help(self.choice, user_menu)
        if not func_return:
            print "Pleace check yout input"
            return
        print "[{:}]".format(func_return)
        if self.choice == 'ul':
            func_return = self.user_lognin()
        elif self.choice == 'ur':
            func_return = self.user_register()
        elif self.choice == 'q':
            func_return = self.exit_note()
        if func_return:
            print "[{:}]\n\n".format("SUCCESS")
        else:
            print "[{:}]\n\n".format("FAILURE")

    def user_lognin(self):
        """user login"""
        name = raw_input("[name] ")
        password = raw_input("[password] ")
        password = hashlib.md5(password).hexdigest()
        if name and password and self.remove_controller(name, password):
            self.user = name
            return True
        else:
            return False

    def user_register(self):
        """user register"""
        name = raw_input("[name] ")
        password = raw_input("[password] ")
        password = hashlib.md5(password).hexdigest()
        if name and password:
            return self.remove_controller(name, password)
        else:
            return False

    def main_func(self):
        """main func"""
        main_menu = (
            ('an', 'add Note'),
            ('dn', 'delete Note by title'),
            ('da', 'delete all Note'),
            ('la', 'list all Note'),
            ('lt', 'list Note by title'),
            ('lk', 'list Note by keyword'),
            ('et', 'edit Note title'),
            ('ec', 'edit Note content'),
            ('q', 'quit Note')
        )
        while self.choice != 'q':
            self.show_menu(main_menu)
            self.choice = raw_input("NoteBook $ ")
            self.exec_choice_main(main_menu)

    def exec_choice_main(self, main_menu):
        """exec the choice"""
        func_return = self.show_help(self.choice, main_menu)
        if not func_return:
            print "Pleace check yout input"
            return
        print "[{:}]".format(func_return)
        if self.choice == 'an':
            func_return = self.add_note()
        elif self.choice == 'dn':
            func_return = self.delete_note()
        elif self.choice == 'da':
            func_return = self.delete_all_note()
        elif self.choice == 'la':
            func_return = self.list_all_note()
        elif self.choice == 'lt':
            func_return = self.list_note_by_title()
        elif self.choice == 'lk':
            func_return = self.list_note_by_keyword()
        elif self.choice == 'et':
            func_return = self.update_note_title()
        elif self.choice == 'ec':
            func_return = self.update_note_content()
        elif self.choice == 'q':
            func_return = self.exit_note()
        if func_return:
            print "[{:}]\n\n".format("SUCCESS")
        else:
            print "[{:}]\n\n".format("FAILURE")

    def add_note(self):
        """add note func"""
        title = raw_input("[title] ")
        content = raw_input("[content] ")
        if title and content:
            return self.remove_controller(title, content, self.user)
        else:
            return False

    def delete_note(self):
        """delete note func"""
        title = raw_input("[title] ")
        if title:
            return self.remove_controller(title, self.user)
        else:
            return False

    def delete_all_note(self):
        """delete all note"""
        return self.remove_controller(self.user)

    def list_all_note(self):
        """list all note"""
        self.print_notes(self.remove_controller())
        return True

    def list_note_by_title(self):
        """"list all note by title"""
        title = raw_input("[title] ")
        if title:
            self.print_notes(self.remove_controller(title))
            return True
        else:
            return False

    def list_note_by_keyword(self):
        """list note by key word"""
        keyword = raw_input("[keyword] ")
        if keyword:
            self.print_notes(self.remove_controller(keyword))
            return True
        else:
            return False

    def update_note_title(self):
        """update note title"""
        title = raw_input("[Note title] ")
        new_title = raw_input("[new title] ")
        if title and new_title:
            return self.remove_controller(title, new_title, self.user)
        else:
            return False

    def update_note_content(self):
        """uodate note content"""
        title = raw_input("[Note title] ")
        new_content = raw_input("[new input] ")
        if title and new_content:
            return self.remove_controller(title, new_content, self.user)
        else:
            return False

    def print_notes(self, notes):
        """print notes"""
        if notes:
            for note in notes:
                self.print_note(note)
        else:
            print "[EMPTY]"

    def show_menu(self, menu):
        """main menu"""
        print "{:<56}".format(">NoteBook<")
        for operation_char, operation_help in menu:
            self.print_line(operation_char, operation_help)

    def show_help(self, choice_str, menu):
        """show help"""
        for operation_char, operation_help in menu:
            if operation_char == choice_str:
                return operation_help
        return ""

    def print_note(self, note):
        """print notes"""
        print "[TITLE]  : ", note["title"]
        print "[CONTENT]: ", note["data"]
        print "[OWNER]: ", note["user"]

    def print_line(self, operation_char, operation_help):
        print "{operation_char:<5}- {operation_help:<48}".format(**vars())
