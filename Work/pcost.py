# pcost.py
#
# Exercise 1.27
# Open file
# Skip header
# Loop through the lines
# Convert line to list
# Multiply line[1] to line[2]
# Store running sum to total
# Print total

f = open("Data/portfolio.csv", "rt")
next(f)
total = 0
for line in f:
    row = line.split(",")
    total += int(row[1]) * float(row[-1].strip())
print(total)
