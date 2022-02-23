#!/usr/bin/python3
"""
Display all states which match an argument from db hbtn_0e_0_usa
"""

import MySQLdb


def match_state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
    for rows in cursor.fetchall():
        print(rows)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    match_state()
