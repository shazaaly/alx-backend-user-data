#!/usr/bin/env python3
""" to manage the Basic API authentication.
"""


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
