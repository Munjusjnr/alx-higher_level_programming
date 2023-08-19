#!/usr/bin/python3
#  A script that lists all states from the database hbtn_0e_0_usa
""" script should take 3 arguments: mysql username, mysql password and
    database name (no argument validation needed
    Your code should not be executed when imported
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
