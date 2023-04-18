#!/usr/bin/python3
"""
A script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(username = sys.argv[1], password = sys.argv[2], db_name = sys.argv[3], 
                             host = 'localhost', port = 3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    result = cur.fetchall()
        
    for state in state;
        print(state)
