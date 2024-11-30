"""
CP1404/CP5632 Practical
Quick Picks Lottery Ticket Generator
"""

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate random quick picks for a lottery."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a single line of random numbers for a quick pick."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:  # Ensure no duplicates
            quick_pick.append(number)
    quick_pick.sort()  # Sort numbers in ascending order
    return quick_pick


main()
