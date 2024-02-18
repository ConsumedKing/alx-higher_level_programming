#!/usr/bin/python3
"""
This is Script two in mysql project
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if not states:
        print("Nothing")
    else:
        print(f'{states.id}: {states.name}')
