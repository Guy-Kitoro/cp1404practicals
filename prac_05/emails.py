"""
CP1404/CP5632 Practical
Emails and names program
Estimate: 30 minutes
Actual: 35 minutes
"""


def main():
    """Store and display names and emails from user input."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct == "n":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address."""
    parts = email.split('@')[0]
    name = " ".join(parts.split('.')).title()
    return name


main()
