"""
Names: Alyssa Comstock, Calvin Hoo
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
Description:
"""

import unittest
from task import conv_endian
from task import my_datetime


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

    def test_my_datetime_time_zero(self):
        """
        Function tests the time at 0 seconds.
        """
        test_sec = 0
        expected_date = "01-01-1970"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_last_possible_date(self):
        """
        Function tests the time representing the date 12-31-9999.
        """
        test_sec = 253402296897
        expected_date = "12-31-9999"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_first_leapyear(self):
        """
        Function tests the time representing start of the first
        leap year since the epoch (02-29-1972 at 00:00:00).
        """
        test_sec = 68169600
        expected_date = "02-29-1972"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_leapyear_day_after_feb28(self):
        """
        Function tests the time representing the day after the Feb 29th
        in the first leap year. (03-31-1972 at 00:00:00)
        """
        test_sec = 68256000
        expected_date = "03-01-1972"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_special_nonleapyear(self):
        """
        Function tests a random day on a year that is divisible by 4
        and is divisible by 100 making this year a non-leap year.
        (09-28-2100 at 00:00:00)
        """
        test_sec = 4125772800
        expected_date = "09-28-2100"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_special_leapyear(self):
        """
        Function tests a random day on a year that is divisible by 4
        and is divisible by 400 making this year a leap year.
        (09-28-2400 at 00:00:00)
        """
        test_sec = 13592880000
        expected_date = "09-28-2400"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_last_leapyear_before9999(self):
        """
        Function tests a random time on the last leap year
        before year 9999. (06-12-9996 at 00:00:00)
        """
        test_sec = 253290153600
        expected_date = "06-12-9996"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_new_years(self):
        """
        Function tests the exact second that a new year starts.
        (01-01-2900 at 00:00:00)
        """
        test_sec = 29348006400
        expected_date = "01-01-2900"
        self.assertEqual(my_datetime(test_sec), expected_date)

    def test_my_datetime_second_before_new_years(self):
        """
        Function tests the exact second before a new year starts.
        (12-31-2899 at 23:59:59)
        """
        test_sec = 29348006399
        expected_date = "12-31-2899"
        self.assertEqual(my_datetime(test_sec), expected_date)


if __name__ == '__main__':
    unittest.main()
