#!/usr/bin/env python3
"""_summary_
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
