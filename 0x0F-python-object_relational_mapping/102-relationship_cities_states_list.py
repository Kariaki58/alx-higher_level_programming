#!/usr/bin/python3
"""important module"""
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    queryContent = session.query(City, State).join(State).all()
    for c, s in queryContent:
        print(f"{c.id}: {c.name} -> {s.name}")
    session.commit()
    session.close()
