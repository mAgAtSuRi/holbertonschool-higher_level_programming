#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=user, password=password, db=db_name
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE states.name LIKE BINARY '{}'"
        "ORDER BY states.id ASC".format(state_name)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
