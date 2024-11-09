def main():
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items!")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    total_price = 0.0

    for i in range(num_items):
        while True:
            try:
                price = float(input(f"Price of item {i + 1}: "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                total_price += price
                break
            except ValueError:
                print("Please enter a valid number.")

    if total_price > 100:
        total_price *= 0.9  # Apply a 10% discount

    print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()
