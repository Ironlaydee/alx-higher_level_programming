#!/usr/bin/python3
""" A script that list all 'states' frkm the database 'hbtn_0_0e_usa:
"""

import sys
import MySQLdb


def list_all():
    '''list all states in db'''
    user,password,db=argv[1],argv[2],argv[3],host='localhost',port=3306
    db = MySQLdb.connect(host=host, user=username, passwd=password, 
                             db=db_name, port=port)
    cur = db.cursor() 
    cur.execute('SELECT * FROM states ORDER BY id ASC;') 
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)
