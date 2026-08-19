# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    "Computes the total cost of a portfolio file"
    total = 0
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)  # Ignore header
        for row in rows:
            total += int(row[1]) * float(row[-1])
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
