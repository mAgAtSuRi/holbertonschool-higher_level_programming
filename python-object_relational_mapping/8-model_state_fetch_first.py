#!/usr/bin/python3
"""
This module contain query for getting all
instances of a class State
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()  # creation d'une sessions

    # réalisation d'une query Select id, name from state order by id où id =1
    # ici, pas besoin de boucle car on récupère le 1er résultat
    state = session.query(State).filter(State.id == 1).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Not found")

    session.close()
    engine.dispose()