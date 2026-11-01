#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2


    @property
    def position(self):
        """Devuelve postion."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Devuelve valor lados."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Imprime el cuadrado."""
        print(self.__str__())

    def __str__(self):
        """Genera la representación en texto del cuadrado."""
        if self.__size == 0:
            return ""

        rows = []
        # Saltos verticales según position[1]
        for _ in range(self.__position[1]):
            rows.append("")

        # Espacios horizontales según position[0] y '#' según size
        for _ in range(self.__size):
            rows.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(rows)
