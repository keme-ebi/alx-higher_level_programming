#!/usr/bin/python3
"""This module lists all cities of that state from the database hbtn_0e_4_usa
after taking the name of a state as an arguments"""


import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states ON states.id \
            = cities.state_id WHERE states.name = %s;", (sys.argv[4], ))

    rows = cur.fetchall()

    for i, row in enumerate(rows):
        print(", ".join(str(value) for value in row), end="")
        if i < len(rows) - 1:
            print(', ', end="")
    print()

    db.close()
