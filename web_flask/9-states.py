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


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """displays state lists and cities with id"""
    states = storage.all("State")
    if state_id is not None:
        state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the db storage upon teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
