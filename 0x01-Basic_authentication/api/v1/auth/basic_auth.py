#!/usr/bin/env python3
""" to manage the Basic API authentication.
"""

import base64
from .auth import Auth


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
