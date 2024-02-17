#!/usr/bin/python3
""" This is Script one in mysql project """
import sys
import MySQLdb

connection = MySQLdb.connect(host="localhost",
                             user=sys.argv[1],
                             password=sys.argv[2],
                             database=sys.argv[3],
                             port=3306)

cursor = connection.cursor()
query = "SELECT id, name FROM states ORDER BY id ASC"


cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)


cursor.close()
connection.close()
