import pytest
from src.validator import validate_password_strength

def test_valid_password():
    assert validate_password_strength("Password1!") == True
    assert validate_password_strength("baeILYUME@3") == True
    assert not validate_password_strength("password")  # No number or special character
