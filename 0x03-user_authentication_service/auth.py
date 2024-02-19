#!/usr/bin/env python3
"""
script for _hash_password method
"""

import bcrypt
from db import DB
from user import User


def _hash_password(password):
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password):
        """_summary_
        """
        existing_user = (
            self._db._session.query(User)
            .filter_by(email=email)
            .first()
            )
        if existing_user:
            raise ValueError(f'User {email} already exists.')
        hashed = _hash_password(password)
        new_user = self._db.add_user(email, hashed)
        return new_user
