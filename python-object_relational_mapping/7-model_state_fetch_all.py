#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 4:
    print("Usage: ./7-model_state_fetch_all.py <username> <password> <database>")
    sys.exit(1)

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}",
        pool_pre_ping=True
	)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    
    session.close()