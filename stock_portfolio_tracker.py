# CodeAlpha Task 2 - Stock Portfolio Tracker

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:
    stock = input("\nEnter Stock Name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    choice = input("Do you want to add another stock? (yes/no): ").lower()
    if choice != "yes":
        break

print("\n========== PORTFOLIO ==========")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock} -> {quantity} shares × ${price} = ${value}")

print("------------------------------")
print(f"Total Investment Value = ${total_investment}")

# Save result to CSV
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Total"])

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        writer.writerow([stock, quantity, price, quantity * price])

    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print("\n✅ Portfolio saved successfully in 'portfolio.csv'")