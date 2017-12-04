#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
from notebook.controller import NoteService


class NoteBook(object):
    """NoteBook UI"""

    def __init__(self):
        self.controller = NoteService()
        self.choice = ""
        self.user = ""
        self.user_func()

    def exit_note(self):
        """exit system"""
        self.controller.write_data()
        self.user = ""
        return True

    def user_func(self):
        """user system"""
        user_menu = (
            ('a', 'user sign in '),
            ('r', 'user register'),
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
        if self.choice == 'a':
            func_return = self.user_lognin()
        elif self.choice == 'r':
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
        if name and password and self.controller.user_lognin(name, password):
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
            return self.controller.create_user(name, password)
        else:
            return False

    def main_func(self):
        """main func"""
        main_menu = (
            ('a', 'add Note'),
            ('d', 'delete Note by title'),
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
        if self.choice == 'a':
            func_return = self.add_note()
        elif self.choice == 'd':
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
            return self.controller.create_note(title, content, self.user)
        else:
            return False

    def delete_note(self):
        """delete note func"""
        title = raw_input("[title] ")
        if title:
            return self.controller.delete_note(title, self.user)
        else:
            return False

    def delete_all_note(self):
        """delete all note"""
        return self.controller.delete_all_note(self.user)

    def list_all_note(self):
        """list all note"""
        self.print_notes(self.controller.list_all_note())
        return True

    def list_note_by_title(self):
        """"list all note by title"""
        title = raw_input("[title] ")
        if title:
            self.print_notes(self.controller.querry_note_by_title(title))
            return True
        else:
            return False

    def list_note_by_keyword(self):
        """list note by key word"""
        keyword = raw_input("[keyword] ")
        if keyword:
            self.print_notes(self.controller.querry_note_by_keyword(keyword))
            return True
        else:
            return False

    def update_note_title(self):
        """update note title"""
        title = raw_input("[Note title] ")
        new_title = raw_input("[new title] ")
        if title and new_title:
            return self.controller.update_note_title(title, new_title, self.user)
        else:
            return False

    def update_note_content(self):
        """uodate note content"""
        title = raw_input("[Note title] ")
        new_content = raw_input("[new input] ")
        if title and new_content:
            return self.controller.update_note_data(title, new_content, self.user)
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
        print "[TITLE]  : ", note.title
        print "[CONTENT]: ", note.data
        print "[OWNER]: ", note.user

    def print_line(self, operation_char, operation_help):
        print "{operation_char:<5}- {operation_help:<48}".format(**vars())
