# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    "Computes the total cost of a portfolio file"
    total = 0
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)  # Ignore header
        for row in rows:
            total += int(row[1]) * float(row[-1])
    return total


print(portfolio_cost("Data/portfolio.csv"))
