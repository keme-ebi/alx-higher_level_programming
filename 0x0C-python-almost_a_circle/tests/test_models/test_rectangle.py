#!/usr/bin/python3
"""Unittest for Rectangle class
"""
from io import StringIO
from contextlib import redirect_stdout
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
        rt = Rectangle(10, 2)
        rb = Rectangle(4, 3)
        self.assertEqual(rt.id, rb.id - 1)
        self.assertEqual(rt.width, 10)
        self.assertEqual(rt.height, 2)
        self.assertEqual(rt.x, 0)
        self.assertEqual(rt.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_passing_strings_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            Rectangle('1', 1)
        with self.assertRaises(TypeError):
            Rectangle(1, '1')
        with self.assertRaises(TypeError):
            Rectangle(1, 1, '1')
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 'y')

    def test_passing_floats_to_instances_except_id(self):
        with self.assertRaises(TypeError):
            Rectangle(4.4, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2.2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.3)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1.5)

    def test_arg_more_than_expected(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 2, 3, 2, 2)

    def test_access_private_instances(self):
        Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            Rectangle.__width
        with self.assertRaises(AttributeError):
            Rectangle.__width
        with self.assertRaises(AttributeError):
            Rectangle.__x
        with self.assertRaises(AttributeError):
            Rectangle.__y

    def test_arg_with_tuples_list_sets(self):
        with self.assertRaises(TypeError):
            Rectangle([1], 1)
        with self.assertRaises(TypeError):
            Rectangle(1, {1})
        rl = Rectangle(1, 1, (1))
        self.assertEqual(rl.x, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, {2})

    def test_arg_negative_numbers(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_arg_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)


class TestRectangleArea(unittest.TestCase):

    def test_area(self):
        r5 = Rectangle(3, 2)
        self.assertEqual(r5.area(), 6)
        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)
        r5 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r5.area(), 56)

class TestRectangleDisplay(unittest.TestCase):

    def test_display(self):
        expected_output = "##\n##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            rd = Rectangle(2, 2)
            rd.display()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_display_when_x_or_y_or_both_are_present(self):
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            rd = Rectangle(2, 3, 2, 2)
            rd.display()
            self.assertEqual(buffer.getvalue(), expected_output)

class TestRectangleSTRMethod(unittest.TestCase):

    def test_str_mehthod(self):
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            rs = Rectangle(4, 6, 2, 1, 12)
            print(rs)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_str_method_with_no_id_added(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5, 1)
            rse = Rectangle(4, 4)
            expected_output = "[Rectangle] ({}) 1/0 - 5/5\n".format(rse.id - 1)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

class TestRectangleUpdateMethod(unittest.TestCase):

    def test_normal_method_instances_except_id(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs = Rectangle(10, 10, 10, 10)
            rse = Rectangle(5, 5)
            expected_output = "[Rectangle] ({}) 10/10 - 10/10\n".format\
                (rse.id - 1)
            print(rs)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_id_only(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5)
            rs2.update(89)
            expected_output = "[Rectangle] ({}) 0/0 - 5/5\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_id_height_and_width(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(10, 10)
            rs2.update(89, 2, 3)
            expected_output = "[Rectangle] ({}) 0/0 - 2/3\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_id_height_width_and_x(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(10, 10)
            rs2.update(89, 2, 3, 4)
            expected_output = "[Rectangle] ({}) 4/0 - 2/3\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_all_instances(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(10, 10)
            rs2.update(89, 2, 3, 4, 5)
            expected_output = "[Rectangle] ({}) 4/5 - 2/3\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_without_kwargs(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 1)
            rs2.update(89)
            expected_output = "[Rectangle] ({}) 0/0 - 5/1\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_height_kwarg(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5)
            rs2.update(89)
            rs2.update(height=1)
            expected_output = "[Rectangle] ({}) 0/0 - 5/1\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_with_width_and_x(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5)
            rs2.update(89)
            rs2.update(width=1, x=2)
            expected_output = "[Rectangle] ({}) 2/0 - 1/5\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_update_method_of_with_width_y_x_and_id(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5)
            rs2.update(y=1, width=2, x=3, id=89)
            expected_output = "[Rectangle] ({}) 3/1 - 2/5\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_all_instances_with_kwargs(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(5, 5)
            rs2.update(89)
            rs2.update(x=1, height=2, y=3, width=1)
            expected_output = "[Rectangle] ({}) 1/3 - 1/2\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_adding_both_args_and_kwargs(self):
        with StringIO() as buffer, redirect_stdout(buffer):
            rs2 = Rectangle(10, 10, 10, 10)
            rs2.update(89, height=1)
            expected_output = "[Rectangle] ({}) 10/10 - 10/10\n".format(rs2.id)
            print(rs2)
            self.assertEqual(buffer.getvalue(), expected_output)

class TestRectangleToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        expected_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        rt = Rectangle(10, 2, 1, 9, 1)
        rtd = rt.to_dictionary()
        self.assertDictEqual(rtd, expected_output)

    def test_to_dictionary_check_type(self):
        expected_output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        rt = Rectangle(10, 2, 1, 9, 1)
        rtd = rt.to_dictionary()
        self.assertEqual(type(rtd), dict)

if __name__ == "__main__":
    unittest.main()
