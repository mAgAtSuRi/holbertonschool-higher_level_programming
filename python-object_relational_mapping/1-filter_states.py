#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=user, password=password, db=db_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%'\
                   ORDER BY states.id ASC")
    all_states = cursor.fetchall()
    for state in all_states:
        print(state)
