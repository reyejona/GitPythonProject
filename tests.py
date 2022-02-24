"""
Names: Alyssa Comstock
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
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

    def test_little_endian_posi_2(self):
        """
        Function that tests returning the little endian hex value of
        a positive decimal number 123.
        Expected Hex value should be a string of '7B'
        This is the same as the big endian format, since it's only
        a 1 byte section.
        """
        self.assertEqual(conv_endian(123, 'little'), '7B')

    def test_dec_hex_zero_value(self):
        """
        Function that tests if decimal value of 0 properly is converted
        in to the correct hex value.  That is, a decimal value of 0
        should be 00 in hex.
        """

        self.assertEqual(conv_endian(0), '00')

    def test_endian_incorrect(self):
        """
        Test that sees is the incorrect endian value is correctly
        returned as None from the conv_endian function.
        """

        self.assertEqual(conv_endian(-954786, 'small'), None)

    def test_negative_big_endian_value_1(self):
        """
        Function that tests if a decimal value of -954786 properly
        returns a negative value. -954786 would be -0E 91 A2 in
        big endian.
        """

        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_negative_little_endian_value_1(self):
        """
        Function that tests if a decimal value of -954786 properly
        returns a negative value. -954786 would be -A2 91 0E in
        little endian.
        """

        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')


if __name__ == '__main__':
    unittest.main()
