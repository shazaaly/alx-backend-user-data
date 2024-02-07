#!/usr/bin/env python3
"""_summary_
"""

from ast import List
import re
import logging
from typing import List



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        redact the message of LogRecord instance
        Args:
        record (logging.LogRecord): LogRecord instance containing message
        Return:
            formatted string
        """
        message = super().__init__(self.FORMAT)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted

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
