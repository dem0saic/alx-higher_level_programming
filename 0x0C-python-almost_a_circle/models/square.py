#!/usr/bin/python3
"""
Contains the Square class, which implements
a square and inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.

    Attributes:
        size: The size of the square.
        x: The x-coordinate of the square's position.
        y: The y-coordinate of the square's position.
        id: The unique identity of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Returns: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable number of non-keyword arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Returns the string representation of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Returns the dictionary representation of the Square.
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
