#!/usr/bin/env python3
"""
create a SQLAlchemy model named User
for a database table named users
(by using the mapping declaration of SQLAlchemy).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """ SQLAlchemy model representing the 'users' table.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)
