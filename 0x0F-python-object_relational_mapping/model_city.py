#!/usr/bin/python3
"""Defining a class city that inherits from base
Will use the SQLAlchemy module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents the class definition of a city
    id: class attribute id that represents a column of an auto-generated,
       unique integer, can’t be null and is a primary key
    name: class attribute name that represents a column of a string with
        max 128 chars and can’t be null
    state_id: class attribute state_id that represents a column of an integer,
        can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
