#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def empty_list(self):
        self.assertEqual(max_integer(), None)

    def negative_number(self):
        self.assertEqual(max_integer([-10, -1, -3]), -1)

    def multiple_max(self):
        self.assertEqual(max_integer([1, 2, 2, 0]), 2)

    def error_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "word"])
