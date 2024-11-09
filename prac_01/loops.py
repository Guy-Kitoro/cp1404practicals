# Display all the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()  # New line after the odd numbers

# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # New line after counting in 10s

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # New line after counting down

# c. Print n stars. Ask the user for a number, then print that many stars (*)
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()  # New line after stars

# d. Print n lines of increasing stars
for i in range(1, n + 1):
    print('*' * i)  # Print increasing lines of stars