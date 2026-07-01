"""
This module contains the User class, which represents a user in the system. 
The User class has attributes such as username, email, and password, and 
methods for authentication and user management.
"""
import re

class User:
    """
    A class to represent a user in the system.

    Attributes
    ----------
    username : str
        The username of the user.
    email : str
        The email address of the user.
    password : str
        The password of the user.

    Methods
    -------
    authenticate(password):
        Authenticates the user by comparing the provided password with the stored password.
    """

    def __init__(self, username, email, password):
        """
        Constructs all the necessary attributes for the User object.

        Parameters
        ----------
        username : str
            The username of the user.
        email : str
            The email address of the user.
        password : str
            The password of the user.
        """
        self.username = username
        self.email = email
        self.password = password

    def validate_email(self):
        """
        Validates the email address of the user.

        Returns
        -------
        bool
            True if the email address is valid, False otherwise.
        """
        
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None