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

class TestBaseSaveToFile(unittest.TestCase):

    @classmethod
    def tearDown(self):
        try:
            os.remove('Rectangle.json')
        except FileNotFoundError:
            pass
        try:
            os.remove('Square.json')
        except FileNotFoundError:
            pass

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 5, 3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_empty(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_single_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_empty(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_single_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

class TestBaseFromJsonString(unittest.TestCase):

    def test_from_empty_string_rectangle(self):
        self.assertEqual([], Rectangle.from_json_string(None))

    def test_from_empty_string_square(self):
        self.assertEqual([], Square.from_json_string(None))

    def test_from_list_rectangle(self):
        lists = [{'id': 89, 'width': 10, 'height': 4}]
        r1 = Rectangle.to_json_string(lists)
        self.assertTrue(list, Rectangle.from_json_string(r1))

    def test_from_list_square(self):
        lists = [{'id': 89, 'x': 10, 'y': 7, 'size': 4}]
        s1 = Square.to_json_string(lists)
        self.assertTrue(list, Square.from_json_string(s1))

    def test_from_2_list_rectangle(self):
        lists = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        rs = Rectangle.to_json_string(lists)
        self.assertTrue(list, Rectangle.from_json_string(rs))

    def test_from_2_list_rectangle(self):
        lists = [{'id': 89, 'x': 10, 'size': 4}, {'id': 7, 'y': 1, 'size': 7}]
        ss = Square.to_json_string(lists)
        self.assertTrue(list, Square.from_json_string(ss))

class TestBaseCase(unittest.TestCase):

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_not_equals_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 5, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (2) 5/1 - 3", str(s2))
        self.assertEqual("[Square] (2) 5/1 - 3", str(s1))

    def test_create_not_equals_square(self):
        s1 = Square(3, 5, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

class TestBaseLoadFromFile(unittest.TestCase):

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_load_from_rectangle_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output[0]))

    def test_load_from_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertEqual(str(s1), str(output[0]))

    def test_load_from_no_file_square(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_no_file_rectangle(self):
        output = Rectangle.load_from_file()
        self.assertEqual([], output)

if __name__ == "__main__":
    unittest.main()
