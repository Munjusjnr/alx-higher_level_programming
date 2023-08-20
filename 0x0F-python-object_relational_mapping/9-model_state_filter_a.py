#!/usr/bin/python3
"""A script that lists all state objects that contain char a from the database
script would take 3 arguments: mysql username, mysql password and
database name
Usage of the module SQLAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
                           f'@localhost:3306/{sys.argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if "a" in state.name:
            print(f"{state.id}: {state.name}")
