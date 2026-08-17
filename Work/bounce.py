# bounce.py
#
# Exercise 1.5

height = 100
num_bounces = 0

while num_bounces < 10:
    height *= 3 / 5
    print(round(height, 4))
    num_bounces += 1
