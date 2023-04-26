#!/usr/bin/python3
"""Unittest for Rectangle class
"""
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestSquareInstances(unittest.TestCase):

    def test_if_square_is_subclass_of_base(self):
        self.assertEqual(issubclass(Square, Base), True)

    def test_if_square_is_subclass_of_rectangle(self):
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_1_arg(self):
         s1 = Square(1)
         self.assertEqual(s1.size, 1)

    def test_2_args(self):
        st = Square(10, 2)
        sb = Square(4, 3)
        self.assertEqual(st.id, sb.id - 1)
        self.assertEqual(st.size, 10)
        self.assertEqual(st.x, 2)
        self.assertEqual(st.y, 0)

        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 0)

    def test_passing_strings_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            Square('1', 1)
        with self.assertRaises(TypeError):
            Square(1, '1')
        with self.assertRaises(TypeError):
            Square(1, 1, '1')

    def test_passing_floats_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            Square(4.4, 1)
        with self.assertRaises(TypeError):
            Square(1, 2.2)
        with self.assertRaises(TypeError):
            Square(1, 1, 1.3)
        with self.assertRaises(TypeError):
            Square(1, 1, 1.5)

    def test_arg_more_than_expected(self):
        with self.assertRaises(TypeError):
            Square(1, 1, 2, 3, 2)

    def test_access_private_instances(self):
        Square(1)
        with self.assertRaises(AttributeError):
            Square.__size

    def test_private_width(self):
        Square(5)
        with self.assertRaises(AttributeError):
            Square.__width

    def test_private_height(self):
        Square(2)
        with self.assertRaises(AttributeError):
            Square.__height

    def test_private_x(self):
        Square(7)
        with self.assertRaises(AttributeError):
            Square.__x

    def test_private_y(self):
        Square(8)
        with self.assertRaises(AttributeError):
            Square.__y

    def test_arg_with_tuples_list_sets(self):
        with self.assertRaises(TypeError):
            Square([1], 1)
        with self.assertRaises(TypeError):
            Square(1, {1})
        sl = Square(1, 1, (1))
        self.assertEqual(sl.y, 1)
        with self.assertRaises(TypeError):
            Square(1, 1, {2}, 1)

    def test_arg_negative_numbers(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_arg_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

class TestSquareArea(unittest.TestCase):

    def test_area(self):
        s5 = Square(3)
        self.assertEqual(s5.area(), 9)
        s5 = Square(2, 4, 5)
        self.assertEqual(s5.area(), 4)
        s5 = Square(8, 4)
        self.assertEqual(s5.area(), 64)

class TestSquareDisplay(unittest.TestCase):

    def test_display(self):
        expected_output = "##\n##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            sd = Square(2)
            sd.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_with_x(self):
        expected_output = "  ##\n  ##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            sd = Square(2, 2)
            sd.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_when_x_or_y_or_both_are_present(self):
        expected_output = "\n\n  ##\n  ##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            sd = Square(2, 2, 2)
            sd.display()
            self.assertEqual(buffer.getvalue(), expected_output)

class TestSquareSTRMethod(unittest.TestCase):

    def test_str_mehthod(self):
        expected_output = "[Square] (12) 6/2 - 4\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            ss = Square(4, 6, 2, 12)
            print(ss)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_str_method_with_no_id_added(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5, 5, 1)
            sse = Square(4, 4)
            expected_output = "[Square] ({}) 5/1 - 5\n".format(sse.id - 1)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

class TestSquareUpdateMethod(unittest.TestCase):

    def test_normal_method_instances_except_id(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss = Square(10, 10, 10)
            sse = Square(5, 5)
            expected_output = "[Square] ({}) 10/10 - 10\n".format(sse.id - 1)
            print(ss)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_id_only(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5)
            ss2.update(89)
            expected_output = "[Square] ({}) 0/0 - 5\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_id_size_and_x(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(10)
            ss2.update(89, 2, 3)
            expected_output = "[Square] ({}) 3/0 - 2\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_all_instances(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(10)
            ss2.update(89, 2, 3, 4)
            expected_output = "[Square] ({}) 3/4 - 2\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_without_kwargs(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5)
            ss2.update(89)
            expected_output = "[Square] ({}) 0/0 - 5\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_size_kwarg(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5)
            ss2.update(89)
            ss2.update(size=1)
            expected_output = "[Square] ({}) 0/0 - 1\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_size_and_x(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5, 5)
            ss2.update(89)
            ss2.update(size=1, x=2)
            expected_output = "[Square] ({}) 2/0 - 1\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_kwargs_with_all_instances(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(5, 5)
            ss2.update(y=1, size=2, x=3, id=89)
            expected_output = "[Square] ({}) 3/1 - 2\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_adding_both_args_and_kwargs(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            ss2 = Square(10, 10, 10)
            ss2.update(89, size=1)
            expected_output = "[Square] ({}) 10/10 - 10\n".format(ss2.id)
            print(ss2)
            self.assertEqual(buffer.getvalue(), expected_output)

class TestSquareToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        expected_output = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        st = Square(10, 2, 1, 1)
        std = st.to_dictionary()
        self.assertDictEqual(std, expected_output)

    def test_to_dictionary_check_type(self):
        expected_output = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        st = Square(10, 2, 1, 9)
        std = st.to_dictionary()
        self.assertEqual(type(std), dict)

if __name__ == "__main__":
    unittest.main()
