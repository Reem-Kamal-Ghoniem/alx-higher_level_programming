#!/usr/bin/python3
""" a script that  lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    connection.close()
