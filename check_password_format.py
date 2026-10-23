
from database.db import get_connection

conn = get_connection()

if conn is not None:
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users LIMIT 1")
        row = cursor.fetchone()

        if row is None:
            print("The users table is empty.")
        else:
            value = row[0]
            if isinstance(value, bytes):
                value = value.decode("utf-8", errors="replace")

            if value.startswith(("$2a$", "$2b$", "$2y$")):
                print("Existing password format: bcrypt")
            elif value.startswith("pbkdf2:"):
                print("Existing password format: Werkzeug PBKDF2")
            elif value.startswith("scrypt:"):
                print("Existing password format: Werkzeug scrypt")
            else:
                print("Password format is not yet identified.")

        cursor.close()
    finally:
        conn.close()
