#!/usr/bin/python3
"""
Delete a state in a database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

def delet_st():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).filter(State.name.contains('a')).all()
    for el in record:
        session.delete(el)
    session.commit()
    session.close()

if __name__ == "__main__":
    delet_st()
