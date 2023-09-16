#!/usr/bin/python3
"""get all states from a database."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    getAllData = cursor.fetchall()
    for data in getAllData:
        print(data)
    cursor.close()
    db.close()
