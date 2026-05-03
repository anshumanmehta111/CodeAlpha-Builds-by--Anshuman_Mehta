stock_prices = {
    # US Stocks
    "AAPL": 180,     # Apple
    "TSLA": 250,     # Tesla
    "GOOGL": 140,    # Google
    "MSFT": 320,     # Microsoft
    "AMZN": 135,     # Amazon
    "NVDA": 450,     # Nvidia
    "META": 300,     # Meta (Facebook)
    
    # Indian Stocks
    "RELIANCE": 2900,
    "TCS": 3800,
    "INFY": 1500,
    "HDFCBANK": 1600,
    "ICICIBANK": 950,
    "SBIN": 750,
    "ADANIENT": 3100
}
# Stock Tracker with Profit/Loss
print("Welcome to the Stock Portfolio Tracker!")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
      # Display available stocks and their current prices
# Step 1: Current stock prices (market price)

portfolio = {}

print("Enter your stocks (type 'done' to finish):")

# Step 2: Input
while True:
    stock = input("Enter stock name: ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not found!")
        continue
    
    qty = int(input(f"Enter quantity of {stock}: "))
    buy_price = float(input(f"Enter BUY price of {stock}: "))
    
    portfolio[stock] = {
        "quantity": qty,
        "buy_price": buy_price
    }

# Step 3: Calculation
total_investment = 0
current_value = 0
total_profit_loss = 0

print("\nYour Portfolio Analysis:")
print("--------------------------------------------------")

for stock, data in portfolio.items():
    qty = data["quantity"]
    buy_price = data["buy_price"]
    current_price = stock_prices[stock]
    
    invested = qty * buy_price
    current = qty * current_price
    profit_loss = current - invested
    
    total_investment += invested
    current_value += current
    total_profit_loss += profit_loss
    
    status = "Profit 📈" if profit_loss > 0 else "Loss 📉"
    
    print(f"{stock} | Qty: {qty}")
    print(f"Buy: {buy_price} | Current: {current_price}")
    print(f"P/L: {profit_loss:.2f} ({status})")
    print("--------------------------------------------------")

# Step 4: Summary
print("\n📊 Overall Summary")
print(f"Total Invested: {total_investment:.2f}")
print(f"Current Value: {current_value:.2f}")
print(f"Total Profit/Loss: {total_profit_loss:.2f}")

if total_profit_loss > 0:
    print("Overall: Profit 🚀")
elif total_profit_loss < 0:
    print("Overall: Loss ⚠️")
else:
    print("Break-even 😐")