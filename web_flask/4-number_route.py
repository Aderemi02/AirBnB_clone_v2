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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays C and content in text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """displays Python and content in text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def python(n):
    """displays number only if integer"""
    if int(n):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
