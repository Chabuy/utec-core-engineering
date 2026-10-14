#!/usr/bin/env python3

def islower(c):
    ascii_code = ord(c)
    if ascii_code >= 65 and ascii_code <= 90:
        return False
    elif ascii_code >= 97 and ascii_code <= 122:
        return True
    else:
        return False

valor = input("ingrese letra para saber si es minúscula: ")
result = islower(valor)
print(result)
