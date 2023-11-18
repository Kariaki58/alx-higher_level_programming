#!/usr/bin/python3
"""model city fetch state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """entry point"""
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                 sys.argv[2],
                                                 sys.argv[3]),
        echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(
        State, State.id == City.state_id
        ).all()
    for data1, data2 in query:
        print(f"{data1.name}: ({data2.id}) {data2.name}")
    session.commit()
    session.close()
