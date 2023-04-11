#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_normalinput(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_addition_in_list(self):
        self.assertEqual(max_integer([1, 3, 4 + 2, 2]), 6)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 7, 5, 3]), 7)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -4, -10, -20]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([30, 10, 2]), 30)

    def test_max_at_end(self):
        self.assertEqual(max_integer([12, 14, 20]), 20)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, 3, -10, 2]), 3)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_zero_args(self):
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
