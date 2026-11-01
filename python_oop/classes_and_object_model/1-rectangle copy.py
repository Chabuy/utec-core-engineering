#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Rectangle:
    """Representa un rectangulo."""
    def __init__(self, width=0, height=0, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        """Devuelve valor ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Devuelve valor alto."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    
    def my_print(self):
        """Imprime el cuadrado."""
        print(self.__str__())

    def __str__(self):
        """Genera la representación en texto del cuadrado."""
        if self.__width == 0:
            return ""

        rows = []
        # Saltos verticales según position[1]
        for _ in range(self.__position[1]):
            rows.append("")

        # Espacios horizontales según position[0] y '#' según size
        for _ in range(self.__size):
            rows.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(rows)
