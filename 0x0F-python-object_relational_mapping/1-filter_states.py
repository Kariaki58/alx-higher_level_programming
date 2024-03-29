#!/usr/bin/python3
"""filter states"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connect = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
        )

    cur = connect.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
                )

    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    connect.close()
