#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from tests.content import Note
from tests.content import NoteStorage


class NoteTest(unittest.TestCase):
    """Test Note"""

    def test_note(self):
        """TEST Note"""
        note = Note("1", "orz", "huang")
        self.assertEqual(note.title, "1")
        self.assertEqual(note.data, "orz")

    def test_read_note(self):
        """TEST NoteStorage"""
        storage = NoteStorage()
        storage.delete_note("")
        self.assertEqual(len(storage.querry_note("")), 0)
        note = Note("aa", "orz", "huang")
        storage.create_note(note)
        self.assertEqual(len(storage.querry_note("")), 1)
        self.assertEqual(storage.querry_note("")[0].data, "orz")
        self.assertEqual(storage.querry_note(
            "WHERE title = 'aa'")[0].data, "orz")
        storage.update_note("WHERE title = '{:}'".format(note.title),
                            "SET data = 'orzz'")
        self.assertEqual(storage.querry_note(
            "WHERE title = 'aa'")[0].data, "orzz")
        self.assertEqual(storage.querry_note(
            "WHERE title LIKE '%aaa%' OR data LIKE '%z%'")[0].data, "orzz")
        storage.delete_note("WHERE title = '" + note.title + "'")
        self.assertEqual(len(storage.querry_note("")), 0)

if __name__ == "__main__":
    TEST_MODEL = unittest.TestLoader().loadTestsFromTestCase(NoteTest)
    unittest.TextTestRunner(verbosity=3).run(TEST_MODEL)
