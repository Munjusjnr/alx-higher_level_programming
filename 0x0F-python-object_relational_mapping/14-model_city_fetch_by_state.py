#!/usr/bin/python3
"""A script that that prints all City objects from the database
script would take 3 arguments: mysql username, mysql password and
database name
Usage of the module SQLAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
                           f'@localhost:3306/{sys.argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    search = session.query(City, State).filter(City.state_id == State.id) \
                    .order_by(City.id)
    for city, state in search:
        print(f"{state.name}: ({city.id}) {city.name}")
