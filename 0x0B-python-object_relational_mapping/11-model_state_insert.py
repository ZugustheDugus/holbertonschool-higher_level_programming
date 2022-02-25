#!/usr/bin/python3
"""
Add a state to a database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

def add_st():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_LA = State(name='Louisiana')
    session.add(st_LA)
    session.commit()
    print(st_LA.id)
    session.close()

if __name__ == '__main__':
    add_st()
