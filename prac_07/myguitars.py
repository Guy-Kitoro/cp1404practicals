"""
CP1404/CP5632 Practical
Program to manage a collection of guitars.
"""

from guitar import Guitar


def main():
    """Main function to manage guitars."""
    guitars = load_guitars("guitars.csv")

    print("These are the guitars:")
    for guitar in guitars:
        print(guitar)

    print("\nLet's add a new guitar.")
    name = input("Name: ")
    while name.strip():
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        name = input("Name: ")

    guitars.sort()
    print("\nSorted list of guitars:")
    for guitar in guitars:
        print(guitar)

    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, year, cost = line.strip().split(",")
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


if __name__ == "__main__":
    main()
