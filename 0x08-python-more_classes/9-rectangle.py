#!/usr/bin/python3

""" Defining a class """


class Rectangle:
    """ A class representing rectangle

        Attributes:
            width: A private instance with optional type
            height: A private instance with optional type

    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        """
        condition to check whether height or width meets int criteria

        Also checking the value to be a real number

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ width getter
            Return:
                width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
            Return:
                the value of the rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter
            Return:
                height of the the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
            Return:
                the value of the rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ A public instance that returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ A public instance that returns the perimeter of the rectangle """
        per_result = (self.__width + self.__height) * 2
        if self.__width == 0 or self.__height == 0:
            per_result = 0
        return per_result

    def __str__(self):
        """ Method that returns the string representation for the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec_string = ""
            for i in range(self.__height):
                if i == self.__height - 1:
                    rec_string += str(self.print_symbol) * self.__width
                else:
                    rec_string += str(self.print_symbol) * self.__width + "\n"
            return rec_string

    def __repr__(self):
        """ Method that returns a string representation for recreation """
        return (f"Rectangle({self.__width:d}, {self.__height:d})")

    def __del__(self):
        """ Returns a message when an instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ A static method that returns a biggest rectangle based on area

            Parameters:
                rect_1: first rectangle
                rect_2: second rectangle

            Raises:
                TypeError: when either of the rectangle are not instances

            Return:
                Either of the two based on the area of the class Rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ A class method that returns a new Rectangle """
        return cls(size, size)
