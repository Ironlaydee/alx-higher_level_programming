#!/usr/bin/python

// A script that lists all states from the database hbtn_0e_0_usa
//

import sys
import MySQLdb

if __name__ == "__main__";
  db = MySQLdb.connect(user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            port=3306
            host='localhost')
  c = db.cursor()
  c.execute("SELECT id, FROM 'states'")
  all states = c.fetchall

  for state in allStates:
      print(state)
      
      c.close()
      db.close()

