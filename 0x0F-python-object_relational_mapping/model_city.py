#!/usr/bin/python3
"""cities in state"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker


class City(Base):
    __tablename__ = "cities"
    id = Column(autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", order_by="City.id", foreign_keys="City.state_id")
