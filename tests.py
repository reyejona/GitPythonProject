"""
Names: Alyssa Comstock, Jonathan Paul Reyes
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
Description:
"""

import unittest
from task import conv_endian, conv_num


class TestCase(unittest.TestCase):
    """
    Tests for conv_num function
    """
    def test_pos_integer(self):
        """
        Function that tests a positive integer string "999442".
        Expected base 10 value should be a 999442
        """
        self.assertEqual(conv_num("999442"), 999442)

    def test_pos_integer2(self):
        """
        Function that tests a positive integer string "23918".
        Expected base 10 value should be a 23918
        """
        self.assertEqual(conv_num("23918"), 23918)

    def test_neg_integer(self):
        """
        Function that tests a negative integer string "-83984".
        Expected base 10 value should be -83984
        """
        self.assertEqual(conv_num("-83984"), -83984)

    def test_neg_float(self):
        """
        Function that tests a negative floating point string "-67.3488".
        Expected base 10 value should be -67.3488
        """
        self.assertEqual(conv_num("-67.3488"), -67.3488)

    def test_pos_float(self):
        """
        Function that tests a positive floating point string "792.990".
        Expected base 10 value should be 792.990
        """
        self.assertEqual(conv_num("792.990"), 792.990)

    def test_float2(self):
        """
        Function that tests a positive floating point string "7736.933121".
        Expected base 10 value should be 736.933121
        """
        self.assertAlmostEqual(conv_num("736.933121"), 736.933121)

    def test_non_string(self):
        """
        Function that tests a non string, integer "4745".
        Expected return should be "None"
        """
        self.assertIsNone(conv_num(4745))

    def test_non_string2(self):
        """
        Function that tests a non string "1j".
        Expected return should be "None"
        """
        self.assertIsNone(conv_num(1j))

    def test_empty(self):
        """
        Function that tests an empty string "".
        Expected return should be "None"
        """
        self.assertIsNone(conv_num(""))

    def test_decimal_points(self):
        """
        Function that tests an string floating point "012.2.14.2023" with > 1 decimals.
        Expected return should be "None"
        """
        self.assertIsNone(conv_num("012.2.14.2023"))

    def test_integer_float(self):
        """
        Function that tests an string floating point with no decimal part.
        Expected base 10 value should be "3455.0"
        """
        self.assertEqual(conv_num('3455.'), 3455.0)

    def test_hex_invalid(self):
        """
        Function that tests an string hex value with invalid characters.
        Expected return should be "None"
        """
        self.assertIsNone(conv_num("0xWAH34WQ"))

    def test_pos_hex(self):
        """
        Function that tests an string positive hex value "0xA".
        Expected return should be equal to int(0xA).
        """
        self.assertEqual(conv_num("0xA"), int(0xA))

    def test_hex_lower(self):
        """
        Function that tests a string positive hex value "0x09ad".
        Expected return should be equal to int(0x09ad).
        """
        self.assertEqual(conv_num("0x09ad"), int(0x09ad))

    def test_pos_hex2(self):
        """
        Function that tests a lowercase string hex value "0x1ab".
        Expected return should be equal to int(0x1ab).
        """
        self.assertEqual(conv_num("0x1ab"), int(0x1ab))

    def test_neg_hex(self):
        """
        Function that tests a negative string hex value "-0x4BCF2".
        Expected return should be equal to int(-0x4BCF2).
        """
        self.assertEqual(conv_num("-0x4BCF2"), int(-0x4BCF2))

    def test_neg_hex2(self):
        """
        Function that tests a negative string hex value "-0x98347abcd".
        Expected return should be equal to int(-0x98347abcd).
        """
        self.assertEqual(conv_num("-0x98347abcd"), int(-0x98347abcd))

    def test_hex_no_0x(self):
        """
        Function that tests a string hex value "12a3b4c5A" which has no 0x prefix
        Expected return should be "None"
        """
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
