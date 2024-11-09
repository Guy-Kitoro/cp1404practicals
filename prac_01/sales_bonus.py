"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get the initial sales input
sales = float(input("Enter sales: $"))

# Loop until a negative number is entered
while sales >= 0:
    # Calculate the bonus based on sales
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus
    else:
        bonus = sales * 0.15  # 15% bonus

    # Print the calculated bonus
    print(f"Bonus: ${bonus:.2f}")

    # Get the next sales input
    sales = float(input("Enter sales: $"))

print("Thank you for using the sales bonus calculator.")
