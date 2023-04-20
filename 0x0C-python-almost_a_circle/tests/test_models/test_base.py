#!/usr/bin/python3
"""Unittest for Base class
"""
import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_if_id_is_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_if_id_is_added(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_with_float(self):
        b4 = Base(6.6)
        self.assertEqual(b4.id, 6.6)

    def test_id_with_string(self):
        self.assertEqual(Base('hi').id, 'hi')

    def test_private_instance(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_id_with_list(self):
        b1 = Base([1])
        self.assertEqual(b1.id, [1])
        b1 = Base([1, 2])
        self.assertEqual(b1.id, [1, 2])

    def test_id_with_tuple(self):
        b1 = Base((1))
        self.assertEqual(b1.id, 1)
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_id_with_dict(self):
        b1 = Base({'i': 1})
        self.assertEqual(b1.id, {'i': 1})

    def test_id_with_sets(self):
        b1 = Base({1, 2})
        self.assertEqual(b1.id, {1, 2})

class TestBaseToJsonString(unittest.TestCase):

    def test_None(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_rectangle_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_square_to_json_string(self):
        s1 = Square(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))


if __name__ == "__main__":
    unittest.main()
