# Question 1: Ask user for their name and write it to 'name.txt' using open and close
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# Question 2: Read the name from 'name.txt' and print a greeting using open and close
file = open("name.txt", "r")
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

# Question 3: Read first two numbers from 'numbers.txt', add them, and print the result
with open("numbers.txt", "r") as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
    result = number1 + number2
    print(result)

# Question 4: Sum all numbers in 'numbers.txt' and print the total
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(total)
