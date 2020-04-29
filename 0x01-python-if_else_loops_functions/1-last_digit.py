#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = (abs(number) % 10)
if number < 0:
    n = n * -1
if n > 5:
    messag = "and is greater than 5"
elif n < 6:
    messag = "and is less than 6 and not 0"
else:
    messag = "and is 0"
print("Last digit of {:d} is {:d} {}".format(number, n, messag))
