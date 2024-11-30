"""
CP1404/CP5632 Practical
Wimbledon champions and countries
Estimate: 50 minutes
Actual: 55 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Process and display Wimbledon champion data."""
    data = load_data(FILENAME)
    champions = count_champions(data)
    countries = collect_countries(data)

    print("\nWimbledon Champions:")
    for champion, count in sorted(champions.items(), key=lambda x: -x[1]):
        print(f"{champion:20} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data(filename):
    """Load data from the Wimbledon CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip header
        return [line.strip().split(',') for line in file]


def count_champions(data):
    """Count how many times each champion has won."""
    champions = {}
    for entry in data:
        champion = entry[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def collect_countries(data):
    """Collect a set of all unique countries with champions."""
    return {entry[1] for entry in data}


main()
