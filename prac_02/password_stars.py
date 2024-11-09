"""Module docstring"""

def main():
    """Main function to check password and display stars."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Prompt user for a valid password and return it."""
    password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))

main()
