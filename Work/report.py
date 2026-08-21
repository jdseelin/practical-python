# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """Computes the total cost (shares * price) of a portfolio file"""
    portfolio = []
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(reader)  # Remove header
        for name, shares, price in reader:
            portfolio.append(
                {"name": name, "shares": int(shares), "price": float(price)}
            )

    return portfolio


def read_prices(filename):
    """Map a csv file into a dict of names to prices"""
    prices = {}
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        for row in reader:
            # Ignore empty rows
            if row:
                prices[row[0]] = float(row[1])
    return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

# Compute total cost of portfolio
total_cost = 0
for s in portfolio:
    total_cost += s["shares"] * s["price"]

# Compute current value of portfolio
total_price = 0
for s in portfolio:
    total_price += s["shares"] * prices[s["name"]]

# print("Current value: {:.2f}".format(total_price))
# print("Gain/Loss: {:.2f}".format(total_cost - total_price))


def make_report(portfolio, prices):
    """Return a list of tuples (name, shares, current_price, change) given a portfolio list and prices dictionary"""
    report = []
    for stock in portfolio:
        name = stock["name"]
        current_price = prices[name]
        change = current_price - stock["price"]
        report.append((name, stock["shares"], current_price, change))
    return report


for r in make_report(portfolio, prices):
    print(r)
