# -*- coding: utf-8 -*-
"""A Simple Flask App main.py

process request and response
"""

import os
import sys
import inspect
from flask import Flask, request
from werkzeug import secure_filename


def insert_path():
    """insert parentdir"""
    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

insert_path()
from PictureToAscii import PictureToAscii

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """sent index html"""
    return app.send_static_file("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """receive file and return ans"""
    if request.method == 'POST':
        pic = request.files['file']
        pic_path = "temp." + secure_filename(pic.filename)
        pic.save(pic_path)
        pir_obj = PictureToAscii()
        response = "<plaintext>" + pir_obj.picture_to_ascii(pic_path, None)
        os.remove(pic_path)
        return response


@app.route('/<path:filename>')
def stacic_file(filename):
    """sent static file"""
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(port=9010)
    # app.run(host="45.32.21.140", port=9010, debug = False)
