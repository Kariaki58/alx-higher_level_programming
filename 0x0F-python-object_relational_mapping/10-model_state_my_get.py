#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """entry point"""
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]),
        echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    data = sys.argv[4]
    query = session.query(State).filter(State.name==data).all()
    if query:
        for data in query:
            print(f"{data.id}: {data.name}")
    else:
        print("Not found")