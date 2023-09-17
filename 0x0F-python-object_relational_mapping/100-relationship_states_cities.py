#!/usr/bin/python3
"""import modules"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import State
from relationship_state import Base


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Obj1 = State(name="California")
    Obj2 = City(name="San Francisco", state=Obj1)
    session.add(Obj1)
    session.add(Obj2)
    session.commit()
    session.close()
