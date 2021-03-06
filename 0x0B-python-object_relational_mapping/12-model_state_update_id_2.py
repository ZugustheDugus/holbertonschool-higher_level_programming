#!/usr/bin/python3
"""
Update a state in a database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

def updat_st():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).filter_by(id=2).first()
    record.name = "New Mexico"
    session.commit()
    session.close()

if __name__ == "__main__":
    updat_st()
