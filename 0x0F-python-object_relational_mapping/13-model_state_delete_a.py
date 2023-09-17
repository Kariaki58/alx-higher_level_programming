#!/usr/bin/python3
"""import modules"""
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    getNames = session.query(State).filter(State.name.ilike('%a%')).all()
    for data in getNames:
        session.delete(data)
    session.commit()
    session.close()
