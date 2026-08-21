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
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total += nshares * price
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename: ")

cost = portfolio_cost(filename)
print("Total cost:", cost)
