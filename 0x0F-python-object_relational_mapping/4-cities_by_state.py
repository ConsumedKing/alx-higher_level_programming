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
    cursor.execute("SELECT cities.id, cities.name ,states.name \
                   FROM states, cities WHERE states.id = cities.state_id")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
