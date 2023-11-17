#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connect = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
        )

    cur = connect.cursor()
    cmd = """
    SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states
    ON cities.state_id=states.id ORDER BY cities.id
    """
    cur.execute(cmd)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    connect.close()
