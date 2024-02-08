#!/usr/bin/env python3
"""
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.

    """
    byt_psd = password.encode()
    salted = bcrypt.hashpw(byt_psd, bcrypt.gensalt())
    return salted


def is_valid(password, hashed_password) -> bool:
    """_summary_

    Args:
        password (_type_): _description_
        hashed_password (bool): _description_

    Returns:
        bool: _description_
    """

    encoded = bcrypt.encode(password)
    return bcrypt.checkpw(encoded, hashed_password)
