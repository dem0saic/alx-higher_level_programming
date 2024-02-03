#!/usr/bin/python3

"""Module defining a Square class."""


class Square:
    """A class that represents a square.

    Attributes:
        __size: The size of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
        area: Calculates the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square.

        Returns:
            int: The square of the size.
        """
        return (self.__size ** 2)