#!/usr/bin/env python3

for i in range (0, 10):
    first_digit= i
    for j in range (i+1, 10):
        last_digit= j
        if first_digit== 8 and last_digit== 9:
            print(f"{first_digit}{last_digit} ", end="")
        else:
            print(f"{first_digit}{last_digit}, ", end="")
 