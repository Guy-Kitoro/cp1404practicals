"""Generate random scores and save results"""

import random

def main():
    """Generate random scores and write results to a file."""
    num_scores = int(input("Enter number of scores to generate: "))
    with open("results.txt", "w") as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)
            result = get_result(score)
            file.write(f"{score} is {result}\n")

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
