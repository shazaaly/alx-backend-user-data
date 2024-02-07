#!/usr/bin/env python3
"""_summary_
"""

from ast import List
import re
import logging
import typing
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Filter sensitive data in a message.
    Args:
        fields (List[str])
        redaction (str)
        message (str)
        separator (str)

    Returns:
        str: The filtered message with the
        sensitive data redacted.
    """

    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
        return message
