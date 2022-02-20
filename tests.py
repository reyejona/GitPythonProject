"""
Names:
Date:
Class: CS362 - Software Engineering II
Assignment:
Description:
"""

import unittest
from task import *


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_big_endian_posi_1(self):
        """
        Function that tests returning the big endian hex value of
        a positive decimal number 954786.
        Expected Hex value should be a string of '0E 91 A2'
        """

        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_big_endian_posi_2(self):
        """
        Function that tests returning the big endian hex value of
        a positive decimal number 123.
        Expected Hex value should be a string of '7B'
        """

        self.assertEqual(conv_endian(123), '7B')

    def test_big_endian_posi_3(self):
        """
        Function that tests returning the big endian hex value of
        a positive decimal number 1.
        Expected Hex value should be a string of '01'
        """

        self.assertEqual(conv_endian(1), '01')

    def test_little_endian_posi_1(self):
        """
        Function that tests returning the little endian hex value of
        a positive decimal number 954786.
        Expected Hex value should be a string of 'A2 91 0E'
        """

        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')


if __name__ == '__main__':
    unittest.main()
