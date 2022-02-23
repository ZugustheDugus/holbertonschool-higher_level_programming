#!/usr/bin/python3
"""
Display all states which match an argument from db hbtn_0e_0_usa
"""

import MySQLdb
import sys


def match_state():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", [format(sys.argv[4])])
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    match_state()
