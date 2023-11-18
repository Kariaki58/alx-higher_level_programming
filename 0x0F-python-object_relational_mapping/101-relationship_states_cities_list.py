#!/usr/bin/python3
"""list relationship"""
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
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()

    query_data = session.query(State).outerjoin(City).order_by(
        State.id, City.id
        ).all()

    for data in query_data:
        print(f"{data.id}: {data.name}")
        for data in data.cities:
            print(f"    {data.id}: {data.name}")
    
    session.commit()
    session.close() 
