#!/usr/bin/python3
"""This module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initializes a new square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
