# Simple Stock Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

# Number of different stocks
n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock_name = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"{stock_name}: {quantity} shares × ${stock_prices[stock_name]} = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
save = input("Do you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("investment_report.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved to investment_report.txt")