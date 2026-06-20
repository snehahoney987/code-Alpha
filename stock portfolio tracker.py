# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

num_stocks = int(input("Enter number of stocks: "))

for i in range(num_stocks):
    stock_name = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio saved to portfolio.txt")