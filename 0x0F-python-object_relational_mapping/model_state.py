#!/usr/bin/python3
"""Defining a class state that inherits from base
Will use the SQLAlchemy module
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents the class definition of a state
    id: class attribute id that represents a column of an auto-generated,
       unique integer, can’t be null and is a primary key
    name: class attribute name that represents a column of a string with
        max 128 chars and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
