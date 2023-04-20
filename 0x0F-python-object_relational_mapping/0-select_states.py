#!/usr/bin/python3
""" A script that list all 'states' frkm the database 'hbtn_0_0e_usa:
"""
fron sys import argv
import MySQLdb

if __name__ == '__main__': 
    (user,password,db=argv[1],argv[2],argv[3],
    db = MySQLdb.connect(host='localhost', user=user, 
                        passwd=password, db=database)
     
    cur = db.cursor() 
    db.query("SELECT * FROM states ORDER BY id") 
    r = db.store_()
    s = r.fetch_row(maxrow_0)
    for n in s
     print(n)
