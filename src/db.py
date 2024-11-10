import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',        
            password='',
            database='queue_system',
        )
        if conn.is_connected():
            print("Database successfully connected")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None


