#!/usr/bin/python3
"""
list all cities from database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def cities():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
    FROM cities LEFT JOIN states ON cities.state_id=states.id
    WHERE states.name LIKE %s ORDER BY cities.id ASC""", [format(sys.argv[4])])

    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    db.close()

if __name__ == "__main__":
    cities()
