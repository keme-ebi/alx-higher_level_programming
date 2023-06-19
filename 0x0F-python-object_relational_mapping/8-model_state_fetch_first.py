#!/usr/bin/python3
"""lists the first state object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State.id, State.name).first()

    if session.query(State).count() == 0:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
