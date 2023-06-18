#!/usr/bin/python3
"""This module takes an argument and displays all values in the states
from the database hbtn_0e_0_usa where name matches the argument"""


import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{aname}' \
                ORDER BY states.id ASC".format(aname=sys.argv[4]))

    for row in cur.fetchall():
        print(row)

    db.close()
