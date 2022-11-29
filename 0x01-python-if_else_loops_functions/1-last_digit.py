#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number * -1 if number < 0 else number
print(num % 10)
if num % 10 > 5:
    status = "and is greater than 5"
elif num % 10 < 6 and num % 10 > 0:
    status = "and is less than 6 and not 0"
else:
    status = "and is 0"
print(f"Last digit of {number} is {number % 10} {status}")
