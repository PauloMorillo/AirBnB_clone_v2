#!/usr/bin/python3
""" This script starts a flask application to storage all data in mysql"""


from flask import Flask, render_template
from models import storage
from models import State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def handleclose(self):
    """ method to handle close session """
    storage.close()


@app.route('/states')
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


@app.route('/states/<string:inid>')
def showstatesbyid(inid):
    """ route to tempplate for showing sstates """
    objects = storage.all(State)
    # print(objects)
    states = dict()
    cities = dict()
    for key, values in objects.items():
        a = key
        if "State" in key:
            if inid == "987654":
                states[key] = values
            else:
                if values.id == inid:
                    states[key] = values
        if "City" in key:
            if values.state_id == inid:
                cities[key] = values
    # print(states)
    # templatedata = {'Objects': objects}
    return render_template("9-states.html", templatedata=cities,
                           states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
