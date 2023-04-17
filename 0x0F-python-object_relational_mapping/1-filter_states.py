#!/usr/bin/python3
"""
A script that lists all states starting with the letter 'N'from the database hbtn_0e_0usa:
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host="localhost")

    c -db.cursor
    c.execute("SELECT * \
    FROM states \ 
    ORDER BY 'id'")
    [print(state) for state in c.fetchball() if state[1][2] == "N"]

