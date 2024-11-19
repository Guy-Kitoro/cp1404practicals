# randoms.py

import random

# Line 1: Generate a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # line 1

# Line 2: Generate a random number between 3 and 10 (step of 2)
print(random.randrange(3, 10, 2))  # line 2

# Line 3: Generate a random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3

# The random number between 1 and 100 inclusive
random_number = random.randint(1, 100)  # Random number between 1 and 100 (inclusive)
print(f"Random number between 1 and 100: {random_number}")
