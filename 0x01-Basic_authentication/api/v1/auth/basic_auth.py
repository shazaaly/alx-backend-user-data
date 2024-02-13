#!/usr/bin/env python3
""" to manage the Basic API authentication.
"""

import base64
import email
from .auth import Auth
from models.base import Base
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Class for basic authentication.

    Args:
        Auth (type): The auth authentication class.
    """
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """_summary_

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            parts = authorization_header.split(' ')
            return parts[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """ returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """_summary_

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        parts = decoded_base64_authorization_header.split(':')
        if len(parts) < 2:
            return (None, None)
        else:
            email = parts[0]
            pswd = parts[1]
            return (email, pswd)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                         str) -> TypeVar('User'):
        """_summary_

        Args:
            self (_type_): _description_
        """
        user = None
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            user = users[0] if user else None
            if user:
                pswd = user.password
                if pswd:
                    if user.is_valid_password(pswd) is True:
                        return user
                else:
                    return None

        except Exception as e:
            raise e
