#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_max_middle(self):
        self.assertEqual(max_integer([4, 2, 10, 1, 3]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([10, -5, 2]), 10)

    def test_negative_number(self):
        self.assertEqual(max_integer([-10, -1, -3]), -1)

    def test_multiple_max(self):
        self.assertEqual(max_integer([1, 2, 2, 0]), 2)

    def test_one_element(self):
        self.assertEqual(max_integer([2]), 2)
