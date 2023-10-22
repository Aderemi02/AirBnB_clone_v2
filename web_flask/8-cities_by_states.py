#!/usr/bin/python3
"""
starting flask web app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
"""flask web instance"""


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays state lists and cities with id"""
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the db storage upon teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
