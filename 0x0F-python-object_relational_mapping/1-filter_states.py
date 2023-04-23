#!/usr/bin/python3
""" a script that  lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


def list_all():
    '''list all states'''

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port) 
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row [1][0] == 'N':
            print(row)

if __name__ == '__main__':
    list_all()
