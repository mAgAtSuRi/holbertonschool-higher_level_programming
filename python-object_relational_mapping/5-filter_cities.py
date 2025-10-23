#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

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
    cursor.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.name ASC
    """, (state_name,))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
