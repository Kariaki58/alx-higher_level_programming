#!/usr/bin/python3
"""
import uses full modules
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
    creates a table and columns
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
