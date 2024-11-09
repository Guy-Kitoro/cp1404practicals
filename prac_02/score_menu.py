"""Score menu program"""

def main():
    """Main function with a menu to handle scores."""
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Result: {get_result(score)}")
        elif choice == 'S':
            print_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

def get_valid_score():
    """Get a valid score from the user between 0 and 100."""
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Invalid score. Must be 0-100.")
        except ValueError:
            print("Please enter a valid number.")

def print_stars(score):
    """Print stars equal to the score value."""
    print('*' * score)

main()
