#!/usr/bin/env python3
"""
script basic flask app
"""

from flask import Flask, request
from flask.json import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_path():
    """ Root path
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    Register new users
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": f"{email}", "message": "user created"})


from auth import Auth


AUTH = Auth()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
