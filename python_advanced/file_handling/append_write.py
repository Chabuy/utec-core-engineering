#!/usr/bin/env python3
"""This is a docstring using triple single quotes."""


def append_write(filename="", text=""):
    """This is a docstring using triple single quotes."""
    with open(filename, "a", encoding="utf-8") as file:
        content = file.write(text)
    return content
