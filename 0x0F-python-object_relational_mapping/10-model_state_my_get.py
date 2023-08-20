#!/usr/bin/python3
"""A script that prints the State object with the name passed as argument
from the database
script would take 4 arguments: mysql username, mysql password,
database name and state name to search (SQL injection free)
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
    found = False
    states = session.query(State)
    for state in states:
        if state.name == sys.argv[4]:
            print(f"{state.id}")
            found = True
            break
    if found is False:
        print("Not found")
