#!/usr/bin/python3
#  A script that lists all states from the database hbtn_0e_0_usa
""" script should take 4 arguments: mysql username, mysql password
    database name and state name searched (no argument validation needed
    You must use the module MySQLdb
    Your script should connect to a MySQL server running on localhost at port
    Your code should not be executed when imported
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(row) for row in cur.fetchall() if row[1] == sys.argv[4]]
