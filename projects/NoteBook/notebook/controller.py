#!/usr/bin/env python
# -*- coding: utf-8 -*-

from notebook.model import NoteStorage
from notebook.model import Note
from notebook.model import User


class NoteService(object):
    """Service"""

    def __init__(self):
        self.model = NoteStorage()

    def write_data(self):
        """After all commit changes"""
        self.model.write_data()

    def create_user(self, name, password):
        """Return: success or not"""
        if self.model.querry_user("WHERE name = '{:}'".format(name)):
            return False
        else:
            self.model.create_user(User(name, password))
            return True

    def user_lognin(self, name, password):
        """Return True if logn in success"""
        return len(self.model.querry_user(
            "WHERE name = '{0:}' and password = '{1:}'".format(name, password)))

    def create_note(self, title, data, user):
        """Return: success or not"""
        if self.model.querry_note("WHERE title = '{:}'".format(title)):
            return False
        else:
            self.model.create_note(Note(title, data, user))
            return True

    def delete_note(self, title, user):
        """Delete the notes by title"""
        return self.model.delete_note(
            "WHERE title = '{0:}' AND user = '{1:}'".format(title, user))

    def delete_all_note(self, user):
        """Delete all the notes"""
        return self.model.delete_note("WHERE user = '{:}'".format(user))

    def list_all_note(self):
        """List all the notes"""
        return self.model.querry_note("")

    def querry_note_by_title(self, title):
        """querry note by title"""
        return self.model.querry_note("WHERE title = '{:}'".format(title))

    def querry_note_by_keyword(self, keyword):
        """querrt note by keyword"""
        return self.model.querry_note(
            "WHERE title LIKE '%{0:}%' OR data LIKE '%{0:}%'".format(keyword))

    def update_note_title(self, title, new_title, user):
        """update note title"""
        querry = "WHERE title = '{0:}' AND user = '{1:}'".format(title, user)
        update = "SET title = '{:}'".format(new_title)
        return self.model.update_note(querry, update)

    def update_note_data(self, title, new_data, user):
        """updata note data"""
        querry = "WHERE title = '{0:}' AND user = '{1:}'".format(title, user)
        update = "SET data = '{:}'".format(new_data)
        return self.model.update_note(querry, update)
