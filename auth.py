
import bcrypt
from database.db import get_connection


def authenticate_user(username, password):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT user_id, username, password_hash
            FROM users
            WHERE username = %s
            """,
            (username.strip(),)
        )

        user = cursor.fetchone()

        if user is None:
            return None

        stored_hash = user["password_hash"]

        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode("utf-8")

        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            return {
                "user_id": user["user_id"],
                "username": user["username"]
            }

        return None

    except Exception as error:
        print(f"Login error: {error}")
        return None

    finally:
        conn.close()
