#!/usr/bin/python3
"""module to test the base class"""
import unittest
from models.base import Base
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """class to test the base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_assignment(self):
        b3 = Base(10)
        self.assertEqual(b3.id, 10)
