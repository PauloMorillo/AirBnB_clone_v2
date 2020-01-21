#!/usr/bin/python3
""" This script starts a flask web application """

from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ This function returns message in index web page """
    # strict_slashes=False
    return "Hello HBNB!"


@app.route('/hbnb')
def BNB():
    """ This function returns message in index web page """
    # strict_slashes=False
    return "HBNB"


@app.route('/c/<text>')
def textva(text):
    """ This function returns message getting a vcariable web page """
    # strict_slashes=False
    msg = "C " + escape(text)
    msg = msg.replace("_", " ")
    return msg

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
