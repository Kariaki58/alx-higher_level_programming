#!/usr/bin/python3
"""list relationship"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                 sys.argv[2],
                                                 sys.argv[3]),
        echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).outerjoin(City).order_by(
        State.id, City.id
        ).all()
    for d1 in query:
        print(f"{d1.id}: {d1.name}")
        for data in d1.cities:
                print(f"    {data.id}: {data.name}")
    session.close() 
