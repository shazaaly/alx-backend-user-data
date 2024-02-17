#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os



@app_views.route('/auth_session/login', methods=['POSTS'], strict_slashes=False)
def auth_session():
    """
    Handle user login
    Return:
        dictionary representation of user if found else error message
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({'error': 'email'}), 400

    if not password or email == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not user or user == []:
        return jsonify({"error": "user not found"}), 400
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response =  user.to_json()
            session_name = os.getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response
        return jsonify({"error": "wrong password"}), 401
