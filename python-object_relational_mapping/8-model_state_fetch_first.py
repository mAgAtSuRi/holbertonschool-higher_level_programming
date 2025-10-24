#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}", pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer explicitement le State avec id=1
    state = session.query(State).filter(State.id == 1).first()

    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()
