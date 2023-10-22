#!/usr/bin/python3
"""
starting flask web app
"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays number only if integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemp(n):
    """displays html page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberOddEven(n):
    """displays html page only if n is an integer"""
    if n % 2 == 0:
        text = "is even"
    else:
        text = "is odd"
    return render_template("6-number_odd_or_even.html", n=n, text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
