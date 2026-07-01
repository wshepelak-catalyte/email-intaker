from src.db import create_user, get_user_by_username, get_user_by_email, update_user_password, verify_unique_profile
from src.user import User
from src.validator import *

def login():
    pass

def register_user():
    while True:
        username = str(input("Enter username: "))
        email = str(input("Enter email: "))
        password = str(input("Enter password: "))

        if not validate_email_format(email):
            print("Invalid email format. Please try again.")
            continue

        if not verify_unique_profile(username, email):
            print("Username or email already exists. Please try again.")
            continue

        if not validate_password_strength(password):
            print("Password does not meet strength requirements. Please try again.")
            continue

        new_user = User(username, email, password)
        if create_user(new_user):
            print("User registered successfully!")
            break
    pass

def main():

    system_user = None # Initialize system_user to None
    

    while True:
        print("Welcome to the User Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user()
            continue
        elif choice == "2":
            system_user = login()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()