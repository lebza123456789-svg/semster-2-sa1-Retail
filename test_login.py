
import getpass
from auth import authenticate_user

username = input("Username: ").strip()
password = getpass.getpass("Password: ")

user = authenticate_user(username, password)

if user:
    print(f"Login successful. Welcome, {user['username']}!")
else:
    print("Invalid username or password.")
