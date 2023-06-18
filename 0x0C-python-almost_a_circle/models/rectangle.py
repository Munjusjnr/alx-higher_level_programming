#!/usr/bin/python3

""" Defining another class inheriting a class """
from models.base import Base


class Rectangle(Base):
    """ A class representing rectangle with base being inherited

    Attributes:
        width: A private instance representing width of the rectangle
        height: A private instance representing height of the rectangle
        x: A private instance with optional type
        y: A private instance with optional type
        id: A private instance with None optional type

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter
        Return:
            width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """ height getter
        Return:
            height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """ getter of x """
        return self.__x

    @property
    def y(self):
        """getter of y """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter
            Return:
                value of rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
            Return:
                value of rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter
            Return:
                 the value of x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter
            Return:
                the value of y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ A public instance method that returns area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ A public instance method that use # to print out  a rectangle """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ method that returns the string representation of the rectangle """
        return ("[Rectangle] {(:d)} {:d}/{:d} - {:d}/{:d}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ method that assigns an argument to each attribute """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ Returning the dictionary representation of a rectangle """
        dictionary = {}
        dictionary["id"] = seif.id
        dictionary["width"] = self.__width
        dictionary["height"] = self.__height
        dictionary["x"] = self.__x
        dictionary["y"] = self.__y
        return dictionary
