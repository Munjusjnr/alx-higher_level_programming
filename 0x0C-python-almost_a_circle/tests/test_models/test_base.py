#!/usr/bin/python3

""" Containing tests for the class base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_with_id(self):
        """ Testing initializer with given id """
        b = Base(id=12)
        self.assertEqual(b.id, 12)

    def test_without_id(self):
        """ Testing initializer without id """
        first = Base()
        second = Base()
        self.assertEqual(first.id, second.id)

    def test_negative_id(self):
        """ Testing initializer with negative id """
        with self.assertRaises(ValueError):
            b = Base(id=-8)

    def test_with_noninteger_id(self):
        """ Testing initializer with non integer id """
        with self.assertRaises(TypeError):
            b = Base(id="wonder")

    def test_nb_objects_increment(self):
        """ Testing nb_objects incrementing correctly """
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)




