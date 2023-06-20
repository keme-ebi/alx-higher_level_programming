#!/usr/bin/python3
"""adds state object Louisiana to the database hbtn_0e_100_usa"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    newst = State(name='California')

    cty = City(name='San Francisco')

    newst.cities.append(cty)

    session.add(newst)
    session.add(cty)

    session.commit()

    session.close()
