"""
CP1404/CP5632 Practical
UnreliableCar class extends Car.
"""

import random
from car import Car

class UnreliableCar(Car):
    """An unreliable car that only drives based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if it passes the reliability check."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0