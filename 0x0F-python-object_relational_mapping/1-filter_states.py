#!/usr/bin/python3
"""
Script to list states with names starting with 'N' from the
database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extracting MySQL credentials from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connecting to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the SQL query to retrieve states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetching all the results
    results = cursor.fetchall()

    # Displaying the results
    for row in results:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
