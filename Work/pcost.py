# pcost.py
#
# Exercise 1.27

f = open("Data/portfolio.csv", "rt")
next(f)
total = 0
for line in f:
    row = line.split(",")
    total += int(row[1]) * float(row[-1].strip())
print(total)
