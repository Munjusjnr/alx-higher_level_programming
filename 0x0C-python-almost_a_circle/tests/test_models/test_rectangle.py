#!/usr/bin/python3

""" Containing tests for the class rectangle which inherits another class """
import unittest
import sys
import json
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


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

    def test_id_is_None(self):
        """ Testing when no id is given """
        self.assertIsNone(self.rectangle.id)

    def test_invalid_width(self):
        """ Testing invalid width type """
        with self.assertRaises(TypeError):
            self.rectangle.width = "wow"

    def test_negative_width(self):
        """ Testing negative width value """
        with self.assertRaises(ValueError):
            self.rectangle.width = -8

    def test_invalid_height(self):
        """ Testing invalid height type """
        with self.assertRaises(TypeError):
            self.rectangle.height = "bloop"

    def test_negative_height(self):
        """ Testing invalid height value """
        with self.assertRaises(ValueError):
            self.rectangle.height = -2

    def test_invalid_x(self):
        """ Testing invalid x type """
        with self.assertRaises(TypeError):
            self.rectangle.x = "woo"

    def test_negative_x(self):
        """ Testing invalid x value """
        with self.assertRaises(ValueError):
            self.rectangle.x = -7

    def test_invalid_y(self):
        """ Testing invalid y type """
        with self.assertRaises(TypeError):
            self.rectangle.y = "something"

    def test_negative_y(self):
        """ Testing invalid y value """
        with self.assertRaises(ValueError):
            self.rectangle.y = -89

    def test_display_mode(self):
        """ Testing the display mode when given parameters are provided """
        self.rectangle = Rectangle(5, 10)
        output = StringIO()
        sys.stdout = output
        self.rectangle.display()
        sys.stdout = sys.__stdout__
        expect_output = "#####\n" * 10
        self.assertEqual(output.getvalue(), expect_output)

    def test_update_args(self):
        """ Testing when given arguments on the command line """
        self.rectangle.update(1, 6, 7, 8, 9)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 7)
        self.assertEqual(self.rectangle.x, 8)
        self.assertEqual(self.rectangle.y, 9)

    def test_update_kwargs(self):
        """ Testing when given command-line arguments """
        self.rectangle.update(id=1, width=6, height=7, x=8, y=9)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 7)
        self.assertEqual(self.rectangle.x, 8)
        self.assertEqual(self.rectangle.y, 9)

    def test_str(self):
        rectangle_mode = str(self.rectangle)
        expected_mode = "[Rectangle] (1) 9/4 - 5/8"
        self.assertEqual(rectangle_mode, expected_mode)

    def test_dictionary_mode(self):
        """ Testing dictionary-like mode """
        self.rectangle = Rectangle(5, 6, 7, 8, 9)
        rectangle_dict = self.rectangle.to_dictionary()
        expected_dict = {"id": 5, "width": 6, "height": 7, "x": 8, "y": 9}
        self.assertDictEqual(rectangle_dict, expected_dictionary)
