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
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()
    for data, data2 in query:
        print(f"{data2.id}: {data2.name} -> {data.name}")
    session.commit()
    session.close()
