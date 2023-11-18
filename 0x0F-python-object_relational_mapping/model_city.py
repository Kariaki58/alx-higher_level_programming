#!/usr/bin/python3
"""cities in state"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker


class City(Base):
    __tablename__ = "cities"
    id = Column(autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", order_by="City.id", foreign_keys="City.state_id")


if __name__ == "__main__":
    engine = create_engine(
        "mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}", echo=False
        )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    session.commit()
    session.close()
