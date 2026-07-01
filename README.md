# Email Intaker

Email Intaker is a small Python command-line application that demonstrates how regular expressions can be used to validate user input for registration and authentication workflows. The project combines simple form validation with a lightweight SQLite-backed user store to showcase practical regex usage in a beginner-friendly way.

## Overview

This project focuses on two common validation scenarios:

- Validating email addresses with a regular expression
- Checking password strength using pattern-based rules

It also includes a basic user management flow with registration, login, and account information display.

## Features

- Email format validation using regex
- Password strength validation
- User registration and login flow
- SQLite persistence for user profiles
- Unit tests for core validation behavior

## Project Structure

- src/validator.py: Contains the regex-based validation functions
- src/main.py: Implements the interactive command-line interface
- src/db.py: Handles SQLite database operations for user storage
- src/user.py: Defines the User model
- tests/: Contains automated tests for validation logic

## Requirements

- Python 3.8 or newer
- pytest (for running tests)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd email-intaker
   ```

2. Install the test dependency:
   ```bash
   pip install pytest
   ```

## Usage

Initialize the database and start the application:

```bash
python .\src\db.py
python .\src\main.py
```

When the program starts, you can:

- Register a new account
- Log in with an existing account
- View account information
- Exit the application

## Validation Rules

The application currently validates:

- Email addresses using a regex pattern that checks for a username, @ symbol, and domain structure
- Passwords that are at least 8 characters long and contain both a number and a special character

## Testing

Run the test suite with:

```bash
pytest -q
```

## Example

A valid email example:

```text
User@example.com
```

An invalid email example:

```text
User
```

## License

This project is intended for educational and demonstration purposes.

