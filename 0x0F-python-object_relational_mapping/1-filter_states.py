#!/usr/bin/python3
"""This module lists all states with a name starting with
N from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name COLLATE utf8mb4_bin LIKE \
            'N%' ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    db.close()
