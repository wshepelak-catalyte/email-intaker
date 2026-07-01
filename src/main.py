from src.db import create_user, get_user_by_username, get_user_by_email, update_user_password
from src.user import User
from src.validator import *

def login():
    pass

def register_user():
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
        elif choice == "2":
            system_user = login()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()