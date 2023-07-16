#!/usr/bin/python3
""" Module for testing the  Rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
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

    def test_display(self):
        r = Rectangle(3, 5)
        res = "###\n###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display2(self):
        r = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), res)

        r.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        r = Rectangle(5, 4, 2, 3)
        output = "[Rectangle] (1) 2/3 - 5/4"
        result = str(r)
        self.assertEqual(result, output)

    def test_str2(self):
        r = Rectangle(3, 2, 8, 8, 10)
        out = "[Rectangle] (10) 8/8 - 3/2"
        result = str(r)
        self.assertEqual(result, out)

        r.id = 1
        r.width = 7
        r.height = 15
        output = "[Rectangle] (1) 8/8 - 7/15"
        result = str(r)
        self.assertEqual(result, output)

    def test_str3(self):
        r = Rectangle(5, 10)
        out = "[Rectangle] (1) 0/0 - 5/10"
        result = str(r)
        self.assertEqual(result, out)

        r2 = Rectangle(25, 86, 4, 7)
        out = "[Rectangle] (2) 4/7 - 25/86"
        result = str(r2)
        self.assertEqual(result, out)

        r3 = Rectangle(1, 1, 1, 1)
        out = "[Rectangle] (3) 1/1 - 1/1"
        result = str(r3)
        self.assertEqual(result, out)

    def str_test3(self):
        r = Rectangle(3, 3)
        out = "[Rectangle] (1) 0/0 - 3/3"
        result = str(r)
        self.assertEqual(result, out)

    def test_display_with_offset(self):
        r = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        r1 = Rectangle(4, 2)
        res = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ####\n    ####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ####\n    ####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update_with_args_and_kwargs(self):
        r = Rectangle(5, 5)
        r.update(1, 10, x=0)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 1)
        dictionary = r.to_dictionary()
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)
