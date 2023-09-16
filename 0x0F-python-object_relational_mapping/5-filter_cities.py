#!/usr/bin/python3
"""Write a script that takes in the name of a state as
an argument and lists all cities of that state"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
    cur = connection.cursor()
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    results = cur.fetchall()
    row_city = ", ".join(row[0] for row in results)
    print(row_city)

    cur.close()
    connection.close()
