#!/usr/bin/python3
import MySQLdb
from sys import argv

connect = MySQLdb.connect(
    user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
    )

cur = connect.cursor()

cur.execute("SELECT * FROM states ORDER BY states.id ASC")

rows = cur.fetchall()

for row in rows:
    print(row)
