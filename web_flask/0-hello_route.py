#!/usr/bin/python3
""" starting a flask web app"""
from flask import Flask


app = Flask(__name__)
""" flask app instance"""


@app.route('/', strict_slashes=False)
def index():
    """displaying Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
