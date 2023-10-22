#!/usr/bin/python3
"""
starting flask web app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import state


app = Flask(__name__)
"""flask web instance"""


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays state lists with id"""
    state = sorted(list(storage.all("State").values()), key=lambda y: y.name)
    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the db storage upon teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
