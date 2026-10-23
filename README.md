# SecurePass Auditor

A beginner-friendly Python cybersecurity project that evaluates password quality using five configurable rules and generates a password audit report.

## Project Overview

SecurePass Auditor checks whether a password meets basic requirements related to length, numbers, special symbols, uppercase letters, and lowercase letters.

The program displays a report showing which rules pass or fail, calculates a score out of five, and assigns a basic rating.

## Features

- Checks whether the password contains at least 8 characters.
- Checks for at least one number.
- Checks for at least one special symbol.
- Checks for at least one uppercase letter.
- Checks for at least one lowercase letter.
- Calculates a score out of 5.
- Displays a basic password rating.
- Hides password input in the terminal using Python's `getpass` module.
- Includes automated unit tests using Python's built-in `unittest` module.

## Technologies Used

- **Language:** Python
- **Modules:** `string`, `getpass`, `unittest`
- **Editor:** Visual Studio Code

All modules used by the application and its tests are included in Python's standard library. No third-party packages are required.

## Project Structure

```text
SecurePass-Auditor/
├── password_auditor.py
├── test_password_auditor.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3
- A terminal or command prompt
- Visual Studio Code (optional)

## How to Run

1. Download or clone the project.
2. Open the project folder in a terminal.
3. Run the application:

```bash
python password_auditor.py
```

4. Enter a sample password when prompted.
5. Review the audit report.

Note: Password input is hidden while typing. This is normal behavior.

## Example Output

```text
--- SecurePass Auditor Report ---
Minimum 8 characters: PASS
Contains a number: PASS
Contains a special symbol: PASS
Contains uppercase letter: PASS
Contains lowercase letter: PASS

Score: 5/5
Password rating: Strong by configured rules
```

The example above illustrates a password that passes all five configured rules. It is not a recommendation to use that password in a real account.

## Running the Tests

Run the automated tests from the project folder:

```bash
python -m unittest -v test_password_auditor.py
```

The tests check password auditing behavior, including a password that meets all five rules, a short password, a missing number, and a missing special symbol.

## Limitations

- The score reflects only the five configured rules.
- A high score does not guarantee that a password is secure.
- The application does not check password reuse, known password breaches, or lists of commonly used passwords.
- The application does not estimate resistance to every type of password attack.
- This is an educational command-line project, not a complete password-security solution.

## Future Improvements

Possible future improvements include checking against common weak passwords, adding more automated test cases, and developing a graphical user interface.

## Disclaimer

This project is intended for educational purposes. Do not enter your real account passwords into demonstration tools or share sensitive passwords in screenshots, source code, or public repositories.

## Author

Developed as a beginner Python cybersecurity project to practise password auditing, functions, dictionaries, and automated testing.
