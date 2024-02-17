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
    query = "SELECT id, name FROM states WHERE name LIKE BINARY\
        '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
