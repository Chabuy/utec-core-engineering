#!/usr/bin/env python3

for letra in range(ord("a"), ord("z") + 1):
    if chr(letra) != "q" and chr(letra) != 'e':
        print("{}".format(chr(letra)), end="")
