#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test list

    Args:
        unittest (inherit): gotten from unittest module
    """
    def test_list(self):
        """double test lists and None
        """
        data = []
        MainInput = [1, 2, 3, 4]
        self.assertEqual(max_integer(data), None)
        self.assertEqual(max_integer(MainInput), 4)
        self.assertEqual(max_integer[7], 7)
    def test_random(self):
        """when the list is not arange
        """
        data = [1, 4, 3, 2]
        self.assertEqual(max_integer(data), 4)
    
    def test_error(self):
        """check if an exception is raised
        """
        data1, data2 = 1, 5 + 3j
        self.assertRaises(TypeError, max_integer, data1)
        self.assertRaises(TypeError, max_integer, data2)
    
    def test_floatingpoint(self):
        """test floating point numbers"""
        numbers = [-3.2, 4.5, 9.3, 8.2]
        self.assertEqual(max_integer(numbers), 9.3)
    
    def test_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([4, -3, 12]), 12)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)

    def test_string(self):
        self.assertEqual(max_integer(""), None)
        #3, 5, 6, 7