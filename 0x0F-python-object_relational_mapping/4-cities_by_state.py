#!/usr/bin/python3
"""cities by states lists all cities from database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities JOIN states WHERE states.id = cities.state_id
            ORDER BY cities.id ASC""")
    status = cursor.fetchall()
    for data in status:
        print(data)
    cursor.close()
    db.close()
