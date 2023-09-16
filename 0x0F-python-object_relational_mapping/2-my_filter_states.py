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
    search = argv[4]
    qery = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
    cursor.execute(qery.format(search))
    status = cursor.fetchall()
    for data in status:
        print(data)
    cursor.close()
    db.close()
