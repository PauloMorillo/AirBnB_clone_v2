#!/usr/bin/python3
""" This script starts a flask application to storage all data in mysql"""


from flask import Flask, request_template
from models import storage
from models import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def handleclose():
    """ method to handle close session """
    storage.close()

@app.route('/states_list')
def showstates():
    """ route to tempplate for showing sstates """
    templatedata = {'States': storage.all(State)}
    return request_template("7-states_list.html", **templatedata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
