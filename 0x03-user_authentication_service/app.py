#!/usr/bin/env python3
"""
script basic flask app
"""

from flask import Flask
from flask.json import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_path():
    """ Root path
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
