#!/usr/bin/env python3
""" to manage the session API authentication.
"""

from .auth import Auth
from flask import session
from uuid import uuid4


class SessionAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            id = uuid4()
            self.user_id_by_session_id[str(id)] = user_id
            return str(id)
