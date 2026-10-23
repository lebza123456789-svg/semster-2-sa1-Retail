
from database.db import get_connection

conn = get_connection()

if conn is not None:
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW COLUMNS FROM users")

        print("\nExisting users table columns:")
        for column in cursor.fetchall():
            print(f"- {column[0]} | Type: {column[1]} | Null: {column[2]} | Key: {column[3]}")

        cursor.close()

    except Exception as error:
        print(f"Could not inspect users table: {error}")

    finally:
        conn.close()
else:
    print("Database connection failed.")