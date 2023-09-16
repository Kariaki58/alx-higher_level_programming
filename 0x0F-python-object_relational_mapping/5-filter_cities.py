#!/usr/bin/python3
"""cities by states lists all cities from database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    state = (argv[4],)
    cursor = db.cursor()
    cursor.execute(
            """SELECT name FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
            ORDER BY id""", state
            )
    status = cursor.fetchall()
    length = len(status)
    i = 0
    for data in status:
        for col in data:
            print(col, end = '')
        if i < length - 1:
            print(end=', ')
        i = i + 1
    print()
    cursor.close()
    db.close()
