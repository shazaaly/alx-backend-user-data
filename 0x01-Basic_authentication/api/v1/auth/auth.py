#!/usr/bin/env python3
""" to manage the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication system you will implement.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths
            that are excluded from authentication.

        Returns:
            bool: True if authentication is required
            False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header for the given request.

        Args:
            request (Optional): The request object. Defaults to None.

        Returns:
            str: The authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current authenticated user.

        Args:
            request (Optional[Request]):
            The request object representing
            the current HTTP request.

        Returns:
            User: The current authenticated user.

        """
        return None
