#!/usr/bin/python3
"""
import uses full modules
"""
from sqlalchemy import Column, Integer, CHAR, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    creates a table and columns
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
