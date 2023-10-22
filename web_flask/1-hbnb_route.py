#!/usr/bin/python3
"""
starting flask web app
"""
from flask import Flask


app = Flask(__name__)
"""flask web instance"""


@app.route("/", strict_slashes=False)
def index():
    """ displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")