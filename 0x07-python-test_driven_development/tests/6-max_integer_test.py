#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max_integer function """

    def test_max_integer_positive_integers(self):
        """ Testing with positive integers """
        numbers = [4, 5, 6, 7]
        self.assertEqual(max_integer(numbers), 7)

    def test_max_integer_empty_list(self):
        """ Testing with an empty list """
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative_number(self):
        """ Testing with negative numbers """
        numbers = [-7, -6, -5, -4, -3]
        self.assertEqual(max_integer(numbers), -3)

    def test_max_integer_mixed(self):
        """ Testing with mixed real numbers """
        numbers = [-4, 8, 9, 0, -3, -11]
        self.assertEqual(max_integer(numbers), 9)

    def test_max_integer_one_element(self):
        """ Testing with a single element in a list """
        numbers = [32]
        self.assertEqual(max_integer(numbers), 32)

    def test_max_integer_duplicates(self):
        """ Testing with duplicate numbers """
        numbers = [7, 8, 8, 9, 5, 6, 6]
        self.assertEqual(max_integer(numbers), 9)


if __name__ == '__main__':
    unittest.main()
