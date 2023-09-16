#!/usr/bin/python3
"""Filter States"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ASC")
    status = cursor.fetchall()
    for data in status:
        print(data)
    cursor.close()
    db.close()
