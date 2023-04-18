#!/usr/bin/python3
"""
A script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':list_all()
def list_all():
        '''list all states in db'''
            username = sys.argv[1], password = sys.argv[2], db_name = sys.argv[3], host = 'localhost', port = 3306
            db = MySQLdb.connect(user=username, host=localhost, passwd=password, db=db_name, port=port)
            cur = db.cursor()
            cur.execute('SELECT * FROM states ORDER BY id ASC;')
            result = cur.fetchall()
            cur.close()
            db.close()
            if result: for row in result:
                 print(row)
