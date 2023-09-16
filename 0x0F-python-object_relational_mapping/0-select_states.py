#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user="root",
        password="root", database="hbtn_0e_0_usa")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
