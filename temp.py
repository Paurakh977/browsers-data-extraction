import datetime

# now = datetime.datetime.now()
# present_day = now.strftime("%A")
# print(present_day)
today = datetime.date.today()
# print(datetime.date.today())

import mysql.connector
import config

# Establish the connection to the database
conn = config.get_connection()

try:
    # Get a cursor
    cursor = conn.cursor()
    
    # Execute the query
    query = "SELECT * FROM app_usage_info"
    cursor.execute(query)
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Iterate over the rows and print the used_date column
    for row in rows:
        if type(row[5])==type(today):
            print(type(row[5]))
            print("yes")
finally:
    # Close the cursor and the connection
    cursor.close()
    conn.close()
