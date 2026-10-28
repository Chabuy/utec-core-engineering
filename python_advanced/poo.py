#!/usr/bin/env python3

class Ticket:
    """Representa un pedido de entradas."""

    def __init__(self, quantity=0):
        self.quantity = quantity

    @property
    def quantity(self):
        """Devuelve la cantidad de entradas."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if type(value) is not int:
            raise TypeError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity must be >= 0")
        self.__quantity = value

order = Ticket(2)
print(order.quantity)

order.quantity = 4
print(order.quantity)