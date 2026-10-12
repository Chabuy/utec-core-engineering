#!/usr/bin/env python3

for i in range (0, 10):
    first_digit= i
    for j in range (i+1, 10):
        last_digit= j
        dig1= str(first_digit)
        dig2= str(last_digit)
        num= int(dig1+dig2)
        if first_digit== 8 and last_digit== 9:
           print("{0:02d}".format(num), end="")
        else:
            print("{0:02d}, ".format(num), end="")
