#!/usr/bin/python3
"""import modules"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).first()
    #for data in results:
    print(f"{results.id}: {results.name}")
    session.commit()
    session.close()
