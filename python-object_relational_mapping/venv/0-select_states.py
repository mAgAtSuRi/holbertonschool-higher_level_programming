#!/usr/bin/python3
"""
    Script to get all states from the database hbtn_0e_0_usa

    ARGUMENTS :
            mysql username
            mysql password
            database name
    SORTED BY :
        ASC states.id
"""
import MySQLdb
import sys


if __name__ == '__main__':
    # Récupère les arguments (pas de validation demandée)
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL sur localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cur = db.cursor()
    # Récupère tous les états triés par id croissant
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
