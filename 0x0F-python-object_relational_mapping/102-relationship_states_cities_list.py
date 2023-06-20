#!/usr/bin/python3
"""lists all city objects from the database hbtn_0e_101_usa"""

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

    join = session.query(City, State).filter(City.state_id == State.id)

    results = join.order_by(City.id.asc()).all()

    for city, state in results:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
