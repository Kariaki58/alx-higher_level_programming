#!/usr/bin/python3
"""
functions
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """entry point"""
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                 sys.argv[2],
                                                 sys.argv[3]),
        echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).outerjoin(City).order_by(
            State.id, City.id
            ).all()
    for state_data in query:
        print(f"{state_data.id}: {state_data.name}")
        for city_data in state_data.cities:
            print(f"    {city_data.id}: {city_data.name}")
    session.close()
