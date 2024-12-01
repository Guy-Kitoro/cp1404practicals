"""
CP1404/CP5632 Practical
Project class for storing information about projects.
"""

class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a Project."""
        return (f"Project({self.name!r}, {self.start_date}, {self.priority}, "
                f"{self.cost_estimate:.2f}, {self.completion_percentage}%)")

    def __str__(self):
        """Return user-friendly string representation of a Project."""
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Sort projects by priority (ascending)."""
        return self.priority < other.priority

