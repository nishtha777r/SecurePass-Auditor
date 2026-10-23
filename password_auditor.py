
import string
import getpass


def audit_password(password):
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Contains a number": any(char.isdigit() for char in password),
        "Contains a special symbol": any(
            char in string.punctuation for char in password
        ),
        "Contains uppercase letter": any(
            char.isupper() for char in password
        ),
        "Contains lowercase letter": any(
            char.islower() for char in password
        ),
    }

    print("\n--- SecurePass Auditor Report ---")

    for requirement, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{requirement}: {status}")

    score = sum(checks.values())
    total = len(checks)

    print(f"\nScore: {score}/{total}")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong by configured rules"

    print(f"Password rating: {strength}")

    # Important: Return the dictionary so unit tests can use it.
    return checks


def main():
    password = getpass.getpass("Enter a sample password to audit: ")

    if not password:
        print("Error: Password cannot be empty.")
        return

    audit_password(password)


if __name__ == "__main__":
    main()
