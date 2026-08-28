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


def make_report(portfolio, prices):
    """Return a list of tuples (name, shares, current_price, change) given a portfolio list and prices dictionary"""
    report = []
    for stock in portfolio:
        name = stock["name"]
        current_price = prices[name]
        change = current_price - stock["price"]
        report.append((name, stock["shares"], current_price, change))
    return report


def print_report(report):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        format_price = "${:.2f}".format(price)  # Add $ sign
        print(f"{name:>10s} {shares:>10d} {format_price:>10} {change:>10.2f}")


def portfolio_report(portfolio_file, prices_file):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")
