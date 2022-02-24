#!/usr/bin/python3
"""
Search for a state in a database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

def search_st():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    st = [format(sys.argv[4])]

    record = session.query(State).filter(State.name.contains(st)).order_by(State.id).all()

    if (record):
        for el in record:
            print("{}".format(el.id))
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    search_st()
