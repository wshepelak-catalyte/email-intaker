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