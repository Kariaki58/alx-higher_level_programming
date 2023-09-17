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
    getName = session.query(State).filter(State.id == 2).first()
    getName.name = "New Mexico"
    session.commit()
    session.close()
