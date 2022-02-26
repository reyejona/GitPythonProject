"""
Names: Alyssa Comstock
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
Description:
"""

import unittest
from task import conv_endian


class TestCase(unittest.TestCase):
    """
    Tests for conv_num function
    """ 
    # test a positive integer
    def test_pos_integer(self):
        self.assertEqual(conv_num("999442"), 999442)

    def test_pos_integer2(self):
        self.assertEqual(conv_num("23918"), 23918)

    # test a negative integer
    def test_neg_integer(self):
        self.assertEqual(conv_num("-83984"), -83984)

    # test a negative floating point number
    def test_neg_float(self):
        self.assertEqual(conv_num("-67.3488"), -67.3488)

    # test a positive floating point number
    def test_pos_float(self):
        self.assertEqual(conv_num("792.990"), 792.990)

    def test_float2(self):
        self.assertAlmostEqual(conv_num("736.933121"), 736.933121)

    # test non string number
    def test_non_string(self):
        self.assertIsNone(conv_num(4745))

    # test non string type invalid
    def test_non_string2(self):
        self.assertIsNone(conv_num(1j))

    # test empty string invalid
    def test_empty(self):
        self.assertIsNone(conv_num(""))

    # test for more than 1 decimal point
    def test_decimal_points(self):
        self.assertIsNone(conv_num("012.2.14.2023"))

    # test a decimal with integer but no decimal part
    def test_integer_float(self):
        self.assertEqual(conv_num('3455.'), 3455.0)

    # test a hexadecimal value with invalid characters
    def test_hex_invalid(self):
        self.assertIsNone(conv_num("0xWAH34WQ"))

    # test a positive hex
    def test_pos_hex(self):
        self.assertEqual(conv_num("0xA"), int(0xA))

    # test lowercase hex
    def test_hex_lower(self):
        self.assertEqual(conv_num("0x09ad"), int(0x09ad))

    # test a lowercase hex 2
    def test_pos_hex2(self):
        self.assertEqual(conv_num("0x1ab"), int(0x1ab))

    # test a negative hex value
    def test_neg_hex(self):
        self.assertEqual(conv_num("-0x4BCF2"), int(-0x4BCF2))

    # negative hex value #2
    def test_neg_hex2(self):
        self.assertEqual(conv_num("-0x98347abcd"), int(-0x98347abcd))

    # Test a hex value without the "0x" prefix
    def test_hex_no_0x(self):
        self.assertIsNone(conv_num("12a3b4c5A"))

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
