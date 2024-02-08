#!/usr/bin/env python3
"""This module provides a logger with redaction for sensitive data.
The module defines a RedactingFormatter class.
This formatter is used to redact sensitive data.
Example usage:
    logger = get_logger()
    logger.info("User logged in: name=john, email=john@example.com")
"""

from ast import List
import re
import os
import mysql.connector
import logging
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that
    redacts sensitive data in log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and redact sensitive data.

        Args:
            record (logging.LogRecord): LogRecord
            instance containing the log message.

        Returns:
            str: The formatted log message with sensitive data redacted.
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    """
    Return a logging.Logger object configured with the RedactingFormatter.

    Returns:
        logging.Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()

    formatter = RedactingFormatter(PII_FIELDS)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Filter sensitive data in a message.

    Args:
        fields (List[str]): The list of sensitive fields to be redacted.
        redaction (str): The redaction string to replace sensitive data.
        message (str): The message containing sensitive data.
        separator (str): The separator used to
        separate key-value pairs in the message.

    Returns:
        str: The filtered message with the sensitive data redacted.
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


def get_db():
    """
    Get the database connection.
    Retrieves the necessary environment
    variables for the database connection
    and creates a connection to the database.
    Returns:
        connection: The connection object to the database.
    """
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME') or 'root'
    db_username = os.environ.get('PERSONAL_DATA_DB_USERNAME')
    db_password = os.environ.get('PERSONAL_DATA_DB_PASSWORD') or ''
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST') or 'localhost'

    # Create a connection to the database
    connection = mysql.connector.connect(user=db_username,
                                         password=db_password,
                                         host=db_host,
                                         database=db_name)
    return connection
