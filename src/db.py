import sqlite3

init_db_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

def create_user(username, email, password):
    """
    Creates a new user in the database with the provided username, email, and password.

    Parameters
    ----------
    username : str
        The username of the new user.
    email : str
        The email address of the new user.
    password : str
        The password of the new user.

    Raises
    ------
    sqlite3.Error
        If there is an error executing the SQL command.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
    finally:
        conn.close()

def get_user_by_username(username):
    """
    Retrieves a user from the database by their username.

    Parameters
    ----------
    username : str
        The username of the user to retrieve.

    Returns
    -------
    tuple or None
        A tuple containing the user's information (id, username, email, password, created_at) if found,
        or None if no user with the given username exists.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    """
    Retrieves a user from the database by their email address.

    Parameters
    ----------
    email : str
        The email address of the user to retrieve.

    Returns
    -------
    tuple or None
        A tuple containing the user's information (id, username, email, password, created_at) if found,
        or None if no user with the given email exists.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_password(username, new_password):
    """
    Updates the password of a user in the database.

    Parameters
    ----------
    username : str
        The username of the user whose password is to be updated.
    new_password : str
        The new password for the user.

    Raises
    ------
    sqlite3.Error
        If there is an error executing the SQL command.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating user password: {e}")
    finally:
        conn.close()

def verify_unique_profile(username, email):
    """
    Verifies that the provided username and email are unique in the database.

    Parameters
    ----------
    username : str
        The username to check for uniqueness.
    email : str
        The email address to check for uniqueness.

    Returns
    -------
    bool
        True if both the username and email are unique, False otherwise.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
    user = cursor.fetchone()
    conn.close()
    return user is None

if __name__ == "__main__":
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(init_db_table)
    conn.commit()
    conn.close()