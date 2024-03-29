#!/usr/bin/python3
"""lists all state objects that contain the lettet a from
the database hbtn_0e_6_usa"""

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

    ag = sys.argv[4]

    state = session.query(State).filter(State.name.like('%' + ag + '%')).all()

    if state:
        for st in state:
            print("{}".format(st.id))
    else:
        print("Not found")

    session.close()
