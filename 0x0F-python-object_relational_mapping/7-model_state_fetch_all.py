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
    content = session.query(State).all()

    for data in content:
        print(f"{data.id}: {data.name}")

    session.commit()
    session.close()
