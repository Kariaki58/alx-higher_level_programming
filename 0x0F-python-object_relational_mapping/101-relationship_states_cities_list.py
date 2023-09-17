#!/usr/bin/python3
"""important modules"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    SqlStatement = session.query(State).outerjoin(City).order_by(
            State.id, City.id).all()
    for data in SqlStatement:
        print(f"{data.id}: {data.name}")
        for session in data.cities:
            print(f"    {session.id}: {session.name}")
