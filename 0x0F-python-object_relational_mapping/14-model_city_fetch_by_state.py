#!/usr/bin/python3
"""import modules"""
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    getAll = session.query(City, State).join(
            State, State.id == City.state_id).all()
    for city, state in getAll:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()
