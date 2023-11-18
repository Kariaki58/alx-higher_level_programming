#!/usr/bin/python3
"""import modules"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sys import argv


Base = declarative_base()


class State(Base):
    """state class

    Args:
        Base (object): inherites from decleartive_base
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
        )
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
