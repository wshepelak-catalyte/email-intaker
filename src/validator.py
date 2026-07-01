import re

def validate_email_format(email: str)->bool:
    """
    Validates the format of an email address.

    Parameters
    ----------
    email : str
        The email address to validate.

    Returns
    -------
    bool
        True if the email address is valid, False otherwise.
    """
    valid_email = re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
    return valid_email is not None

def validate_password_strength(password: str)->bool:
    """
    Validates the strength of a password.

    Parameters
    ----------
    password : str
        The password to validate.

    Returns
    -------
    bool
        True if the password is strong, False otherwise.
    """
    # Check if password is at least 8 characters long
    if re.match(r"^.{8,}$", password) is None:
        return False
    # Check if password contains at least one number and special character
    if not re.search(r"[0-9]", password) or not re.search(r"[!@#$%^&*(),.?\":{}/<>/]", password):
        return False
    return True
