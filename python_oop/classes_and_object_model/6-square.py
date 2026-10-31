#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        symbol = "#"
        width = self.size
        height = self.size
        offset = self.position
        rows = [" " * offset + symbol * width for _ in range(height)]
        result = "\n".join(rows)
        print(result)

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
        """Genera el texto del cuadrado."""
        if self.__size == 0:
            return ""

        texto = ""

        # Líneas verticales vacías (posición Y)
        for _ in range(self.__position[1]):
            texto += "\n"

        # Filas del cuadrado
        for i in range(self.__size):
            texto += " " * self.__position[0]
            texto += "#" * self.__size
            # Agrega salto de línea solo si no es la última fila
            if i < self.__size - 1:
                texto += "\n"

        return texto

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
