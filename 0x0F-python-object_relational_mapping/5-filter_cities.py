#!/usr/bin/python3
"""
a script that list all cities of a state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], 
                       db=sys.argv[3], port=3306, host='localhost')
    
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
            states.id=cities.state_id WHERE states.name LIKE BINARY \ 
            %(states_name)s \ 
            ORDER BY cities.id ASC", {'states_name': sys.argv[4]}) 
    rows = cur.fetchall() 
    if rows is not None:

    print(", ".join([row[0] for row in rows]))
