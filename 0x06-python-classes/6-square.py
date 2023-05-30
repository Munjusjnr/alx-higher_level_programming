#!/usr/bin/python3

""" Defining a class square """


class Square:
    """
    A class representing a square

    Attributes:
        size: A private instance with an optional type
        position: A private instance with tuple-like values
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """
        condition to check instantiation with optional meets int criteria

        Another condition to check whether value is a real number

        """
    @property
    def size(self):
        """ size getter
            Return:
                size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter
            Return:
                value of square size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position getter
            Return:
                position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter and Returns position value of a square """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(v, int) and v >= 0 for v in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ A public instance method that returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ A public instance method that prints character # when called """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
