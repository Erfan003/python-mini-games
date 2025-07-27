# auth/auth_manager.py

import json
import os
from auth.user import User


USER_FILE = 'auth/users.json'


def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as f:
        data = json.load(f)
        return {u: User.from_dict(info) for u, info in data.items()}


def save_users(users: dict):

    with open(USER_FILE, 'w') as f:
        json.dump({u: user.to_dict() for u, user in users.items()}, f, indent=2)


def register(username: str, password: str):
    users = load_users()
    if username in users:
        return False, "username is already exist."
    users[username] = User(username, password)
    save_users(users)
    return True, "sign in"


def login(username: str, password: str):
    users = load_users()
    user = users.get(username)
    if not user:
        return False, "Username not found."
    if user.password != password:
        return False, "Incorrect password."

    return True, user


def auth_flow():
    while True:
        choice = input("1. login \n"
                       "2. signup \n"
                       "choose : ")
        username = input("Username: ")
        password = input("Password: ")

        if choice == "1":
            success, result = login(username, password)
        elif choice == "2":
            success, result = register(username, password)
        else:
            print("Invalid option.")
            continue

        if success:
            print("✅ Successful")
            return result
        else:
            print(f"❌ Error : {result}")



def main():
    pass

if __name__ == '__main__':
    main()