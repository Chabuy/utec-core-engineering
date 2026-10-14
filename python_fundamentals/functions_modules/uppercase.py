#!/usr/bin/env python3

def uppercase(str):
    for value in (str):
        ascii_code = ord(value)
        if ascii_code >= 65 and ascii_code <= 90:
            print (value, end="")
        elif ascii_code >= 97 and ascii_code <= 122:
            mayuscula = (ascii_code - 32)
            print(chr(mayuscula), end="")

resultado = uppercase("Pedro")
