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
    tup = ()
    for row in rows:
        tup = tup + row
    print(*tup, sep=", ")
    cur.close()
    connect.close()