#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sqlite3
import os


class User(object):
    """A Class to store User"""

    def __init__(self, name, password):
        self.name, self.password = name, password


def read_user(tup):
    """A func to make tuple to User"""
    return User(*tup)


class Note(object):
    """A class to store notes"""

    def __init__(self, title, data, user):
        self.title, self.data, self.user = title, data, user


def read_note(tup):
    """A func to make tuple to Note"""
    return Note(*tup)


class NoteStorage(object):
    """A class to store all notes"""

    def __init__(self):
        self.read_data()

    def read_data(self):
        """Read data from disk"""
        newpath = './data'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        self.conn = sqlite3.connect("./data/note.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS notes(title TEXT, data TEXT, user TEXT)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)")

    def write_data(self):
        """Commit the changes"""
        self.conn.commit()
        self.conn.close()

    def create_user(self, user):
        """Create a User"""
        self.cursor.execute("INSERT INTO users VALUES(?, ?)",
                            [user.name, user.password])

    def querry_user(self, filter_str):
        """User filter_str to querry Notes"""
        self.cursor.execute("SELECT * FROM users " + filter_str)
        select_list = self.cursor.fetchall()
        return [read_user(tup) for tup in select_list]

    def create_note(self, note):
        """Create a Note"""
        self.cursor.execute("INSERT INTO notes VALUES(?, ?, ?)",
                            [note.title, note.data, note.user])

    def querry_note(self, filter_str):
        """Use filter_str to querry Notes"""
        self.cursor.execute("SELECT * FROM notes " + filter_str)
        select_list = self.cursor.fetchall()
        return [read_note(tup) for tup in select_list]

    def update_note(self, filter_str, update_str):
        """Update the Notes"""
        self.cursor.execute("UPDATE notes " + update_str + filter_str)
        return 1

    def delete_note(self, filter_str):
        """Delete the Notes"""
        self.cursor.execute("DELETE FROM notes " + filter_str)
        return 1
