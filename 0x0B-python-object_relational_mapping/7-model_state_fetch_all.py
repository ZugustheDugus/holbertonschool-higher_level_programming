#!/usr/bin/python3
"""
Starts linking class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

def mod_stat_fetch():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State).order_by(State.id):
        print('{}: {}'.format(item.id, item.name))

    session.close()
if __name__ == "__main__":
    mod_stat_fetch()
