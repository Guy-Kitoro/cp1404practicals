# Warmup exercise for list operations
numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted values of expressions
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False (because it's a string, not an integer)
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Update the list as instructed
numbers[0] = "ten"  # Replace the first element with the string "ten"
numbers[-1] = 1  # Replace the last element with the number 1

# Perform additional operations
print(numbers[2:])  # Print all elements except the first two
print(9 in numbers)  # Check if 9 is in the list
