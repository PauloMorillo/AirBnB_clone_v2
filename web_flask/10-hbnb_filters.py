#!/usr/bin/python3
""" This script starts a flask application to storage all data in mysql"""


from flask import Flask, render_template
from models import storage
from models import State, City, Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def handleclose(self):
    """ method to handle close session """
    storage.close()


@app.route('/hbnb_filters')
def showfilters():
    """ route to tempplate for showing sstates """
    objects = storage.all(State)
    # print(objects)
    states = dict()
    cities = dict()
    for key, values in objects.items():
        a = key
        if "State" in key:
            states[key] = values
        if "City" in key:
            cities[key] = values
    objects2 = storage.all(Amenity)
    amenities = dict()
    for keya, valuesa in objects2.items():
        if "Amenity" in keya:
            amenities[keya] = valuesa
    # print(states)
    # templatedata = {'Objects': objects}
    return render_template("10-hbnb_filters.html", templatedata=cities,
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
