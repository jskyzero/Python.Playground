# -*- coding: utf-8 -*-
"""file_process.py
read file or write file from file_path
"""

import os

class FileProcess(object):
    """read and write file"""

    def __init__(self, file_path):
        """receive file_path"""
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        self.file_path = file_path

    def open_read_stream(self, read_filename):
        """return  a read_fileObj"""
        return open(self.file_path + '/' + read_filename, 'r')

    def open_write_stream(self, write_filename):
        """return a write fileObj"""
        return open(self.file_path + '/' + write_filename, 'w')
