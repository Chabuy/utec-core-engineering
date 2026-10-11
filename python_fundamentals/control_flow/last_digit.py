#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

digits = list(str(number))
last_digit = digits[-1]

if number > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif number <=5 and number > 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")
