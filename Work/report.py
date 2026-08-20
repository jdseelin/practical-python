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
            portfolio.append((name, int(shares), float(price)))

    return portfolio


print(read_portfolio("Data/portfolio.csv"))
