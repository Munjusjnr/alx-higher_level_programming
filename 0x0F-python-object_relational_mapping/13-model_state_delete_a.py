#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the letter a
from the database
script would take 3 arguments: mysql username, mysql password and database name
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
    session.query(State).filter(State.name.contains('a'))\
           .delete(synchronize_session=False)
    session.commit()
