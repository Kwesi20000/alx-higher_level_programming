#!/usr/bin/python3
"""
Script to change the name of a State object in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Check if the correct number of arguments is provided"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """Extracting MySQL credentials from command line arguments"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """Create an engine to connect to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    """Bind the engine to the Base class"""
    Base.metadata.create_all(engine)

    """Create a session to interact with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query to retrieve the State object with id = 2"""
    state_to_change = session.query(State).filter_by(id=2).first()

    """Change the name to "New Mexico" if the State object is found"""
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()

    """Closing the session"""
    session.close()
