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
        data = []
        MainInput = [1, 2, 3, 4]
        self.assertEqual(max_integer(data), None)
        self.assertEqual(max_integer(MainInput), 4)

        """check if an exception is raised
        """
    def test_error(self):
        data1, data2 = 1, 5 + 3j
        self.assertRaises(TypeError, max_integer, data1)
        self.assertRaises(TypeError, max_integer, data2)