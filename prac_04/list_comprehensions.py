"""
CP1404/CP5632 Practical
List comprehensions
"""

def main():
    """Demonstrate the use of list comprehensions."""
    numbers = [1, 2, 3, 4, 5]

    # Squares of numbers
    squares = [number ** 2 for number in numbers]
    print(squares)

    # Odd numbers
    odds = [number for number in numbers if number % 2 != 0]
    print(odds)

    # Numbers greater than 2
    greater_than_two = [number for number in numbers if number > 2]
    print(greater_than_two)


main()
