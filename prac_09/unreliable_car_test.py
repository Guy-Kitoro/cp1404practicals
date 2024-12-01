"""
CP1404/CP5632 Practical
Test the UnreliableCar class.
"""

from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar class."""
    unreliable_car = UnreliableCar("Old Clunker", 100, 50)
    for i in range(10):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven}km. Odometer: {unreliable_car._odometer}km")


if __name__ == "__main__":
    main()
