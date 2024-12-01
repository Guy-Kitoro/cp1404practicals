"""
CP1404/CP5632 Practical
SilverServiceTaxi class extends Taxi.
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with additional fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the fare including flagfall."""
        return super().get_fare() + self.flagfall
