#!/usr/bin/python3
"""script that takes in the name of a state as an argument and ..."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connect = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
        )

    cur = connect.cursor()
    cur.execute("""
                SELECT name FROM cities WHERE state_id=(
                SELECT id FROM states WHERE name=%s)
                """, (argv[4],))
    rows = cur.fetchall()
    last = None
    for i in range(len(rows) - 1):
        last = rows[i + 1][0]
        for data in rows[i]:
            print(data, end=', ')
    print(last)
    cur.close()
    connect.close()