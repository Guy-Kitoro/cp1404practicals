"""Determine the result for a score"""

import random

def main():
    """Main function to get user score and print result."""
    score = float(input("Enter your score: "))
    print(f"Your result is: {get_result(score)}")

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, result: {get_result(random_score)}")

def get_result(score):
    """Return result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
