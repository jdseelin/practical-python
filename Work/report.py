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
            portfolio.append({"name": name, "shares": shares, "price": price})

    return portfolio


def read_prices(filename):
    """Map a csv file into a dict of names to prices"""
    prices = {}
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        for row in reader:
            # Ignore empty rows
            if row:
                prices[row[0]] = row[1]
    return prices
