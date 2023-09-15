#!/usr/bin/python3
"""a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_ = sys.argv[4]
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
    cur = connection.cursor()
    que = "SELECT * FROM states WHERE name LIKE BINARY\
            '{}' ORDER BY states.id ASC".format(name_)
    cur.execute(que)
    rows = cur.fetchone()
    if rows is not None:
        print(rows)

    cur.close()
    connection.close()
