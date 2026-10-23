
import getpass
import bcrypt
from database.db import get_connection


def register_user():
    username = input("Create username: ").strip()

    if not username or len(username) > 50:
        print("Username must contain 1–50 characters.")
        return

    password = getpass.getpass("Create password (minimum 8 characters): ")

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        return

    confirm = getpass.getpass("Confirm password: ")

    if password != confirm:
        print("Passwords do not match.")
        return

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    conn = get_connection()

    if conn is None:
        print("Could not connect to the database.")
        return

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (username, password_hash)
            VALUES (%s, %s)
            """,
            (username, password_hash)
        )

        conn.commit()
        print(f"User '{username}' registered successfully.")

    except Exception as error:
        conn.rollback()

        if getattr(error, "errno", None) == 1062:
            print("That username already exists. Choose another.")
        else:
            print(f"Registration failed: {error}")

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    register_user()

