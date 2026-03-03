# TASK 2: Stock Portfolio Tracker
# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
# prices.
# ● Simplified Scope:
# ○ User inputs stock names and quantity.
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
# ○ Display total investment value and optionally save the result in a .txt or .csv file.
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional)



stock_prices = {
    "AAPL": 1800,
    "TSLA": 2500,
    "GOOGL": 2800,
    "MSFT": 3000,
    "AMZN": 3300,
    "NVDA": 1450,
    "META": 2860,
}

portfolio = {}


print("="*50)
print("Stock Portfolio Tracker")
print("Available Stocks:")
print("="*50)
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("-"*50)


# Input loop
while True:
    stock = input("Enter Stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("-"*50)
        continue
    while True:
        quantity = input(f"Quantity for {stock}: ")

        if quantity== "":
            print("Quantity required. Please enter the Quantity")
            print("-"*50)
            continue

        try:       
            qty = int(quantity)

            if qty <= 0:
                print("Quantity must be positive.")
                print("-"*50)
                continue
            break
        except ValueError:
            print("Invalid quantity. Enter a number.")
            print("-"*50)

    
    if stock in portfolio:
        portfolio[stock] +=qty
    else:
        portfolio[stock] = qty

    print(f"Added {qty} of {stock}")

    print(f"Current Quantity of {stock} is:{portfolio[stock]}")
    print("-"*50)

# Check empty portfolio
if not portfolio:
    print("No stocks added.")
    print("-"*50)
    exit()
   


# Calculate total investment

total_investment = 0

print("\n" + "=" * 50)
print("-----------------PORTFOLIO SUMMARY----------------")
print("=" * 50)

# Table Header
print(f"{'Stock':<8}{'Qty':<8}{'Price':<12}{'Total':<15}")
print("-"*50)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    total = price * qty
    total_investment += total
    print(f"{stock:<8}{qty:<8}Rs.{price:<12}Rs.{total:<15}")

print("-" * 50)
print(f"Total Investment:  Rs.{total_investment:,}")
print("=" * 50)

# Save to CSV file
save = input("\nSave to file? (yes/no): ").strip().lower()

if save in ("yes", "y"):
    import csv
    filename = "portfolio.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["-----Portfolio Summary-----"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            total = price * qty
            row_text =f"Stock = {stock} \n Quantity = {qty} \n Price of stock = Rs.{price}  \n Total = Rs.{total}"
            writer.writerow([row_text])
            writer.writerow([])
        writer.writerow([f"Total_investment : Rs.{total_investment}"])

print(f"Portfolio saved to {filename} successfully."),