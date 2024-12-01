"""
CP1404/CP5632 Practical
Guitar class for storing information about guitars.
"""


class Guitar:
    """Represent a guitar."""

    def __init__(self, name, year, cost):
        """Construct a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"Guitar({self.name!r}, {self.year}, {self.cost:.2f})"

    def __str__(self):
        """Return user-friendly string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Calculate the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Sort guitars by year (oldest to newest)."""
        return self.year < other.year
