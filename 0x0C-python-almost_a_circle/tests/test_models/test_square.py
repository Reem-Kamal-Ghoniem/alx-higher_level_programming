#!/usr/bin/python3
""" Module for test class of the square"""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """class for testeing the square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_attributes(self):
        self.s1 = Square(5)
        self.s2 = Square(3, 2, 1, 10)
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 1)

        self.assertEqual(self.s2.size, 3)
        self.assertEqual(self.s2.width, 3)
        self.assertEqual(self.s2.height, 3)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s2.id, 10)

    def test_new_squares(self):
        s = Square(1, 1)
        s2 = Square(1, 1)
        self.assertEqual(False, s is s2)
        self.assertEqual(False, s.id == s2.id)

    def test_is_Base_instance(self):
        s = Square(1)
        self.assertEqual(True, isinstance(s, Base))

    def test_is_Rectangle_instance(self):
        s = Square(1)
        self.assertEqual(True, isinstance(s, Rectangle))

    def test_incorrect_amount_attrs(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_incorrect_amount_attrs_1(self):
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_private_attrs_2(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_private_attrs_3(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_private_attrs_4(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y

    def test_valide_attrs(self):
        with self.assertRaises(TypeError):
            s = Square("2", 2, 2, 2)

    def test_valide_attrs2(self):
        with self.assertRaises(TypeError):
            s = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        with self.assertRaises(TypeError):
            s = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_value_attrs2(self):
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_value_attrs_3(self):
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def _area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)
    def _area_2(self):
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def _display(self):
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def _display_2(self):
        r1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def _str(self):
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def _str_2(self):
        r1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def _str_3(self):
        s = Square()
        result = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

        s2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), res)

    def _str_4(self):
        s = Square(3)
        result = "[Square] (1) 0/0 - 3"
        self.assertEqual(s.__str__(), result)

    def _display_3(self):
        s = Square(5, 2, 1)
        result = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

    def _display_4(self):
        s = Square(3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

        s.x = 1
        result = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

        s.y = 2
        result = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

    def _update(self):
        s = Square(3)
        result = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

        s.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

    def _update_2(self):
        s = Square(3)
        result = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

        s.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s)
            self.assertEqual(str_out.getvalue(), result)

    def _update_3(self):
        s1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def _update_4(self):
        s1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'size': 3, 'y': 5}
        s1.update(**dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def _update_5(self):
        s1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            s1.update(**dic)

    def _to_dictionary(self):
        s1 = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_value_square(self):
        with self.assertRaises(ValueError):
            s1 = Square(-1)
