#!/usr/bin/python3
""" This script starts a flask application to storage all data in mysql"""


from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def handleclose(self):
    """ method to handle close session """
    storage.close()


@app.route('/states_list')
def showstates():
    """ route to tempplate for showing sstates """
    objects = storage.all(State)
    # print(objects)
    states = dict()
    for key in objects.items():
        a = key[1]
        if type(a) == State:
            states[a.id] = a.name
    # print(states)
    templatedata = {'States': states}
    return render_template("7-states_list.html", **templatedata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
