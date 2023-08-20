#!/usr/bin/python3
"""A script that takes the name of the state as an argument and lists all
cities of the state using the database  hbtn_0e_4_usa
Script should take 4 arguments: mysql username, mysql password, database name
and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (sys.argv[4],))
    cities = [city[0] for city in cur.fetchall()]
    print(", ".join(cities))
