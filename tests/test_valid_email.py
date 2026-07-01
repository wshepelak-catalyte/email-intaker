import pytest
from src.validator import validate_email_format

def test_valid_email():
    assert validate_email_format("User@example.com") == True

def test_invalid_email():
    assert validate_email_format("User") == False