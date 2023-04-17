#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleInstances(unittest.TestCase):

    def test_if_rectangle_is_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_2_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_passing_strings_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle('1', 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, '1')
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, '1')
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 'y')

    def test_passing_floats_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4.4, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2.2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1.3)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1.5)

    def test_arg_more_than_expected(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 2, 3, 2, 2)

    def test_access_private_instances(self):
        r1 = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(AttributeError):
            r1.__x
        with self.assertRaises(AttributeError):
            r1.__y

    def test_arg_with_tuples_list_sets(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, {1})
        r1 = Rectangle(1, 1, (1))
        self.assertEqual(r1.x, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, {2})

if __name__ == "__main__":
    unittest.main()
