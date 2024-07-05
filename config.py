import mysql.connector
from mysql.connector import Error

def get_connection():
    """Establish and return a new database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="samadhandb"
    )

def insert(tab_name, used_time, browser):
    try:
        conn = get_connection()
        dbcursor = conn.cursor()
        
        dbcursor.execute("SELECT * FROM app_usage_info WHERE tab_name=%s", (tab_name,))
        row = dbcursor.fetchone()
        
        if row: 
            used_time = row[1] + 1  
            dbcursor.execute("UPDATE app_usage_info SET used_time=%s WHERE tab_name=%s", (used_time, tab_name))
        else:
            query = "INSERT INTO app_usage_info (tab_name, used_time, browser) VALUES (%s, %s, %s)"
            values = (tab_name, used_time, browser)
            dbcursor.execute(query, values)
            
        conn.commit()
        print("Data inserted successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn.is_connected():
            dbcursor.close()
            conn.close()
            print("MySQL connection is closed")


