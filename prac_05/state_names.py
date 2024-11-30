"""
CP1404/CP5632 Practical
State names program
"""

STATE_NAMES = {
    "QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
    "WA": "Western Australia", "ACT": "Australian Capital Territory",
    "VIC": "Victoria", "TAS": "Tasmania"
}


def main():
    """Display full state names based on user input or print all states."""
    state = input("Enter short state: ").strip().upper()
    while state != "":
        try:
            print(f"{state} is {STATE_NAMES[state]}")
        except KeyError:
            print("Invalid short state")
        state = input("Enter short state: ").strip().upper()

    print("\nAll States:")
    for short_name, full_name in STATE_NAMES.items():
        print(f"{short_name:3} is {full_name}")


main()
