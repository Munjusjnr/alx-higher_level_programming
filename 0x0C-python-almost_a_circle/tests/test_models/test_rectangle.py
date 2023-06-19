#!/usr/bin/python3

""" Containing tests for the class rectangle which inherits another class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """ Testing with sample rectangle """
        self.rectangle = Rectangle(1, 5, 8, 9, 4)

    def test_id(self):
        """ Testing with id of the rectangle """
        self.assertEqual(self.rectangle.id, 1)

    def test_width(self):
        """ Testing the width of the rectangle """
        self.assertEqual(self.rectangle.width, 5)

    def test_height(self):
        """ Testing the height of the rectangle """
        self.assertEqual(self.rectangle.height, 8)

    def test_x(self):
        """ Testing for x functionality """
        self.assertEqual(self.rectangle.x, 9)

    def test_y(self):
        """ Testing for y functionality """
        self.assertEqual(self.rectangle.y, 4)

    def test_area(self):
        """ Testing for the area of the rectangle """
        self.assertEqual(self.rectange.area, 40)
