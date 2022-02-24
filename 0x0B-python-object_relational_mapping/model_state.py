#!/usr/bin/python3
"""
Connect to a db using SQLAlchemy that contains class, state, and instance
"""


from sqlalchemy import (create_engine, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class Definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
