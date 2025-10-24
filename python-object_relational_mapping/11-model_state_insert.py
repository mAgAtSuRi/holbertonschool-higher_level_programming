#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

	new_state = State(name='Louisiana')
	session.add(new_state)
	session.commit()

	print(new_state.id)
