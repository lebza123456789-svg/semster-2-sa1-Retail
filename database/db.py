
import mysql.connector
from config import db_config


def get_connection():
    try:
        print("Attempting MySQL connection...")
        conn = mysql.connector.connect(**db_config)
        print("Database connected successfully.")
        return conn

    except mysql.connector.Error as error:
        print(f"Database connection failed: {error}")
        return None
