#!/usr/bin/python3
"""
A script that list all cities from a database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306, host="localhost")

    cur = db.cursor()
    cur.execute("SELECT states.name, cities.id, cities.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = cur.fetchall()

for state in states:
        print(state)