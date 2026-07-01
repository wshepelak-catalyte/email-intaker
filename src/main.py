from db import create_user, get_user_by_username, verify_unique_profile
from user import User
from validator import *

def login():
    """
    Prompts the user for their username and password, and attempts to log them in by verifying the credentials against the database.

    Returns
    -------
    User or None
        A User object if the login is successful, or None if the login fails.
    """
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    user_data = get_user_by_username(username)
    if user_data is None:
        print("User not found.")
        return None

    stored_password = user_data[3]  # Assuming the password is the fourth element in the tuple
    if password == stored_password:
        print("Login successful!")
        return User(user_data[1], user_data[2], stored_password)  # Create a User object
    else:
        print("Incorrect password.")
        return None

def register_user():
    """
    Registers a new user by prompting for username, email, and password. Validates the input and creates a new user in the database if all checks pass.
    """
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
        print("3. Account Info")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user()
            continue
        elif choice == "2":
            system_user = login()
        elif choice == "3":
            if system_user:
                print(f"Username: {system_user.username}")
                print(f"Email: {system_user.email}")
            else:
                print("Please log in first.")
        elif choice == "4":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()