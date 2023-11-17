#!/usr/bin/python3
"""import modules"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
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


if __name__ == "__main__":
    engine = create_engine("mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}", echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    session.commit()
    session.close()