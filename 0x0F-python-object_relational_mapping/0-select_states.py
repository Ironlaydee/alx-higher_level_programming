#!/usr/bin/python3
""" A script that list all 'states' frkm the database 'hbtn_0_0e_usa:
"""
import sys
import MySQLdb

if __name__ == '__main__': 
    db = MySQLdb.connect(user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306,
    host='localhost')

    cur = db.cursor() 
    cur.execute("SELECT * FROM states;") 
    states = cur.fetchall() 

    for state in states
        print(state)
