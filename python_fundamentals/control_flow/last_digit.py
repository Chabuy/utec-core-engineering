#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

digits = list(str(number))
last_digit = digits[-1]

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is", end=" ")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is", end=" ")
elif last_digit <= 5 and last_digit > 0:
    print(f"Last digit of {number} is {last_digit} and is", end=" ")
else:
    print(f"Last digit of {number} is -{last_digit} and is", end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
