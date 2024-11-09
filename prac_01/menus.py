def main():
    # Get the user's name
    name = input("Enter name: ")

    # Display the menu and get the user's choice
    choice = ''

    while choice != 'Q':
        print("\n(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ").strip().upper()

        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        elif choice == 'Q':
            continue  # Simply continue to the next iteration to quit
        else:
            print("Invalid choice")

    print("Finished.")


if __name__ == "__main__":
    main()
