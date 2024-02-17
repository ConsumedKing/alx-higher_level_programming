#!/usr/bin/python3
"""
This is Script two in mysql project
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 user=sys.argv[1],
                                 password=sys.argv[2],
                                 database=sys.argv[3],
                                 port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name \
                   FROM states, cities WHERE states.id = cities.state_id \
                   AND states.name LIKE BINARY %s ORDER BY cities.id ASC",
                   (sys.argv[4], ))
    results = cursor.fetchall()
    if results is not None:
        print(", ".join([row[0] for row in results]))
    cursor.close()
    connection.close()
