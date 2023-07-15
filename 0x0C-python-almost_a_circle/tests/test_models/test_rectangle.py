#!/usr/bin/python3
""" Module for testing the  Rectangle class """
import unittest
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ class to test Rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor(self):
        r = Rectangle(2, 4, 1, 3, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 10)

    def test_constructor2(self):
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_constructor3(self):
        r = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(False, r is r2)
        self.assertEqual(False, r.id == r2.id)

    def test_relate_to_base(self):
        r = Rectangle(1, 1)
        self.assertEqual(True, isinstance(r, Base))

    def test_incorrect_amount_of_attributes(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

        with self.assertRaises(TypeError):
            r = Rectangle(2)

    def test_attribute_error(self):
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width

        with self.assertRaises(AttributeError):
            r.__height

        with self.assertRaises(AttributeError):
            r.__x

        with self.assertRaises(AttributeError):
            r.__y

    def test_valid_attr(self):
        with self.assertRaises(TypeError):
            r = Rectangle("3", 3, 3, 3, 3)

        with self.assertRaises(TypeError):
            r = Rectangle(3, "3", 3, 3, 3)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 3, "3", 3, 3)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 3, 3, "3", 3)

    def test_valid_value_attr(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_valid_value_attr2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_valid_value_attr3(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 1, -1)

    def test_valid_value_attr4(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 3, 1, -3)

    def area_test(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def area2_rest(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        r.width = 5
        self.assertEqual(r.area(), 10)
        r.height = 5
        self.assertEqual(r.area(), 25)

    def area3_test(self):
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)
