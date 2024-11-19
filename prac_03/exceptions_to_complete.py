is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # If input is valid, we can set this to True
    except ValueError:  # Catching ValueError for non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)
