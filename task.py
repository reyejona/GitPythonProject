"""
Names: Alyssa Comstock
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
Description:
"""


def conv_num(num_str):
    pass


def my_datetime(num_sec):
    """
    Function that takes an integer value representing the the number of seconds
    since the epoch (Jan 01, 1970) and converts and returns a string containing
    the date from the epoch.
    :param num_sec: The number of seconds since the epoch. Must be positive or
    zero.
    :return: String containing a date from the epoch. Format: MM-DD-YYYY.
    """
    # At time 0, return the first date of the epoch.
    if num_sec == 0:
        return "01-01-1970"

    date_data = {
        "month": None,
        "day": None,
        "year": None,
        "days_since": None,
        "is_leap_year": None
    }
    print(find_year_since_epoch(num_sec))
    print(is_leap_year(1977))
    return

def find_month(num_sec, leapYear):
    """
    """


def find_year(num_sec, date_data):
    """
    Function takes the time in seconds since the epoch and returns the year
    that the date falls on.
    """
    # Calculate the rough number of seconds in a year.
    seconds_in_year = 60 * 60 * 24
    # Calculate the estimated years since the epoch.
    days_since_epoc = int(num_sec // seconds_in_year) + 1
    curr_year = 1970
    
    while days_since_epoc > 365:
        if is_leap_year(curr_year) and days_since_epoc > 366:
            days_since_epoc -= 366
            curr_year += 1
        if not is_leap_year(curr_year):
            days_since_epoc -= 365
            curr_year += 1


def is_leap_year(year):
    """
    Function checks if the time in seconds since the epoch falls on a leap
    year. Returns True if so, False otherwise.
    """
    # To determine if the year falls on a leap year. Subtract 1972 (the first
    # leap year) since the epoch and modulo the difference by 4. The year is a
    # leap year if it is divisible by 4.
    return ((year - 1972) % 4) == 0


def conv_endian(num, endian='big'):
    """
    Function that takes a decimal value and which endian direction it is and
    returns the hex value in whatever endian type it is.
    :param num: decimal value
    :param endian: what direction the hex value goes
    :return: hex value result or None if the endian value is not valid
    """

    if endian != 'big' and endian != "little":
        # check to see if the endian value is valid
        return None

    if num == 0:
        # we do not need to convert to hex
        # since it's always going to be 00
        return '00'

    hex_nums, sign = dec_to_hex_string(num)
    result = format_hex(hex_nums, endian, sign)

    return result


def dec_to_hex_string(num):
    """
    Helper function for the conv_endian function. Takes a decimal value
    and converts it to a hex string
    :param num: decimal value
    :return: string hex value in big endian format
    """

    sign = ''
    if num < 0:
        sign = '-'
        num = abs(num)

    hex_nums = ''
    # At 10-15 inclusive hex values become representations from A-F
    # so, we are going to use a dictionary look up for this.
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while num != 0:
        # Calculate the value first, and the direction will be
        # reversed based on what endian direction it is
        if num % 16 in hex_dict.keys():
            # if the value is between [10,15] inclusive
            # check the hex_dict value
            hex_nums += str(hex_dict[num % 16])
        else:
            # value is less than 10, add it as a string
            hex_nums += str(num % 16)
        num = num // 16

    return hex_nums, sign


def format_hex(hex_nums, endian, sign):
    """
    Helper function that takes the hex value returned from dec_to_hex_string
    which is a string of hex values and formats them in to a string
    where each byte is joined with a space in between. Sign is included
    if the value is negative.
    :param hex_nums: string of values that need to be formatted
    :param endian: direction the bytes need to be arranged
    :param sign: sign of the value positive or negative
    :return: correctly formatted hex string with a space
    in between the bytes and the sign value properly added.
    """

    result = []
    for i in reversed(range(0, len(hex_nums), 2)):
        # get each byte segment which is 2 digit values in the string
        if len(hex_nums[i:i + 2]) < 2:
            # if it is a single digit then a 0 is added
            result.append("0" + hex_nums[i:i + 2])
        else:
            result.append(hex_nums[i:i + 2][::-1])

    if endian == "little":
        # if its little endian the values need to be reversed
        result = result[::-1]

    result[0] = sign + result[0]
    return " ".join(result)


if __name__ == '__main__':
    # print(conv_endian(-123))
    print(my_datetime(253375602708))
