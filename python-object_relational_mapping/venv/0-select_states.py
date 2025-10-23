#!/usr/bin/env python3
"""Lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


def main():
    # Récupère les arguments (pas de validation demandée)
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base MySQL sur localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cursor = db.cursor()
    # Récupère tous les états triés par id croissant
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # nettoyage
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
