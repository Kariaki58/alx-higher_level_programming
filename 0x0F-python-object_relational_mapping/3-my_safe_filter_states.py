#!/usr/bin/python3
"""sql injection..."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    tup = (argv[4],)
    cursor.execute(query, tup)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
