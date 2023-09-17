#!/usr/bin/python3
"""import modules"""
from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).all()
    for data in results:
        print("{}: {}".format(data.id, data.name))
    session.commit()
    session.close()
