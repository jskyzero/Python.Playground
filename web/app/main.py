#!/usr/bin/env python

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/<path:filename>')
def css(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug = True)
    # app.run(host="45.32.21.140", port=8080, debug = False)
