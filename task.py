import re
"""
Group #20
Names: Alyssa Comstock, Calvin Hoo, Jonathan Paul Reyes
Date: March 7, 2022
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow

"""


def conv_num(num_str):
    """
    conv_num()
    Function will receive a string that can represent + or -
    integers, floating point numbers or hexadecimals with prefix 0x
    and convert it to a base 10 number.
    Invalid formats: More than 1 decimal point.Strings with alpha not
    part of hex number. Hex without prefix 0x. Non strings or empty
    strings.
    :param num_str: string of integer/float/hex number
    :returns  base 10 number matching type sent
    """
    negative = False
    decimal = 0
    # check if not a string type or empty strings
    if type(num_str) != str or num_str == '':
        return None
    # check for negative
    if num_str.startswith('-'):
        negative = True
        # cut off the minus sign
        num_str = num_str[1:]
    # check for hexadecimal prefix
    if num_str.startswith('0x'):
        num_str = num_str[2:]  # start after '0x' prefix
        # use regex matching for hexadecimal values
        hex_chars = re.compile("^[0-9a-fA-F]+$")
        # if hexadecimal value found after 0x, it is valid
        if hex_chars.match(num_str):
            return convert_hex(num_str, negative)
        else:
            # if character is not Hex it will return none
            return None
    for i in num_str:
        if i == '.':
            decimal = 1
    # If floating point numbers
    if decimal == 1:
        return convert_float(num_str, negative)
    else:
        # use regex matching for finding valid integers
        integer_digits = re.compile(r"[0-9]+$")
        if integer_digits.match(num_str):
            return convert_integer(num_str, negative)


def convert_hex(num_str, negative):
    """
    convert_hex()
    Helper function will receive a string representing a
    hexadecimal number with prefix "0x" removed. Puts the
    string through a loop where each digit is given a hex
    value and decimal value. The string is then turned
    into a base 10 number.
    :param num_str: string of hex number
            negative: optional sign of value
    :return result_hex: which is the base 10
        representation of the string hex
    """
    result_hex = 0
    # convert string lowercase into uppercase before converting to hex
    # enumerate will give 2 loop variables count (i), and index value (v)
    for i, v in enumerate(num_str.upper()):
        # hex values put in equivalent index from 0-15
        hexadecimal = "0123456789ABCDEF"
        # Convert hex value to decimal value equivalent
        value = hexadecimal.index(v)
        # power of 16 for each hex based on hex string length
        power = (len(num_str) - (i + 1))
        # multiply each hex digit value by the equivalent power of 16
        # add together all values to turn into decimal
        result_hex += (value * 16 ** power)
    if negative:
        return result_hex * -1
    else:
        return result_hex


def convert_integer(num_str, negative):
    """
    convert_integer()
    Helper function will receive a string representing a
    integer and/or negative sign, loop through the string
    multiply each digit by 10 and add together to convert
     it to a base 10 number
    :param num_str: string of integer either + or -
            negative: optional sign of string integer
    :return result_integer: which is the base 10
        representation of the string integer
    """
    result_integer = 0
    for digit in num_str:
        # multiply each digit by 10 and add together to get result
        result_integer *= 10
        for d in '0123456789':
            # while each string digit > d
            # loop through d adding +1
            # then multiply result * 10
            result_integer += digit > d
    if negative:
        return result_integer * -1
    else:
        return result_integer


def convert_float(num_str, negative):
    """
    convert_float()
    Helper function will receive a string representing a
    floating point number and/or negative sign, divide it
    into the integer and decimal part then add together again
    to convert it to a base 10 number
    :param num_str: string of Float either + or -
            negative: sign of string
    :return final_result: which is the base 10 representation
            of the float
    """
    decimal = 0
    # find if there is decimal in num_str
    for char in num_str:
        if char == '.':
            decimal += 1
        if decimal > 1:
            return None
    result_int = 0
    num = 0
    decimal_result = 0
    final_result = 0
    # if string with no decimal, is an integer
    if decimal == 0:
        # num_str should stay the same length
        num = num_str
    if decimal == 1:
        # find the '.' split integer part from decimal part
        num, dec_part = num_str.split('.')
        # convert the integer part
        result_int = convert_integer(num, negative)
        # convert the decimal component
        for digit in dec_part[::-1]:  # remove the decimal point
            # divide each digit by 10 and add together to get result
            decimal_result /= 10
            for d in '0123456789':
                # while each string digit > d
                # loop through d adding +1
                # then divide result /10
                decimal_result += digit > d
    if negative:
        # If neg turn negative to positive before adding to decimal
        result_int = (0 - result_int)
        decimal_result = decimal_result / 10
        final_result = decimal_result + result_int
        return final_result * -1
    if decimal == 1:
        decimal_result = decimal_result / 10
        final_result = decimal_result + result_int
        return final_result
    else:
        return final_result


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

    # Date data object that holds information about the date since epoch.
    date_data = {
        "month": None,
        "day": None,
        "year": None,
        "remain_days": None,
        "is_leap_year": None
    }

    # Calculate and fill the date data object.
    find_year_and_if_leap_year(num_sec, date_data)
    find_month_and_day(date_data)

    # Using the date from date_data, returns the string date in MM-DD-YYYY
    # format.
    return str(date_data["month"]).zfill(2) + "-" + str(date_data["day"])\
        .zfill(2) + "-" + str(date_data["year"])


def find_month_and_day(date_data):
    """
    Function calculates and fills the date_data object with the month
    and day of the date since the epoch.
    :param date_data: dictionary object representing calculated data of the
    target date.
    :return: None.
    """
    # An array representing the non-leap year calender days of each month.
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Get the remaining days from the date_data object.
    remain_days = date_data["remain_days"]

    # Iterate through the calender days and calculate to find month and day.
    for month, days in enumerate(days_in_months):
        # Cannot subtract anymore days. Fill information into date_data object
        # and end iteration.
        if remain_days <= days:
            date_data["month"] = month + 1
            date_data["day"] = remain_days
            break
        # If the current year is a leap year. Handles Feb.
        elif date_data["is_leap_year"] and month == 1:
            # Subtract by 29 if possible.
            if remain_days > 29:
                remain_days -= (days + 1)
            # Not possible to subtract 29. Date falls in Feb.
            else:
                date_data["month"] = month + 1
                date_data["day"] = remain_days
                break
        # Standard calculation.
        else:
            remain_days -= days


def find_year_and_if_leap_year(num_sec, date_data):
    """
    Function takes in the number of seconds since the epoch and a date data
    object and calculates the year the date falls on and whether or not
    the year is a leap year. This information is placed in the date_data
    object.
    :param num_sec: number of seconds since the epoch.
    :date_data: dictionary object representing calculated data of the
    target date.
    :return: None.
    """
    # Calculate the number of seconds in a day.
    seconds_in_day = 60 * 60 * 24
    # Calculate the days since the epoch.
    days_since_epoc = int(num_sec // seconds_in_day) + 1
    curr_year = 1970

    # Find the year and days remaining by subtracting days in each
    # calender year.
    while days_since_epoc > 365:
        # Current year is a leap year. Subtracts 366 days if possible.
        if is_leap_year(curr_year):
            if days_since_epoc > 366:
                days_since_epoc -= 366
                curr_year += 1
            # Break loop if 366 days is not subtractable.
            else:
                break
        # Current year is not a leap year. Subtracts 365 days.
        elif not is_leap_year(curr_year):
            days_since_epoc -= 365
            curr_year += 1

    # Fill date_data with corresponding calculated data.
    date_data["year"] = curr_year
    date_data["remain_days"] = days_since_epoc
    date_data["is_leap_year"] = is_leap_year(curr_year)


def is_leap_year(year):
    """
    Function checks if the time in seconds since the epoch falls on a leap
    year. Returns True if so, False otherwise.
    :param year: Integer value representing the year being examined.
    :return: Bool value True if year is a leap year, False otherwise.
    """
    # Is a leap year if the year is divisble by 4 and either not divisible
    # by 100 or divisible by 400.
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def conv_endian(num, endian='big'):
    """
    Function that takes a decimal value and which endian direction it is and
    returns the hex value in whatever endian type it is.
    :param num: decimal value
    :param endian: what direction the hex value goes
    :return: hex value result or None if the endian value is not valid
    """

    sign = ''
    if endian != 'big' and endian != "little":
        # check to see if the endian value is valid
        return None
    elif num == 0:
        # we do not need to convert to hex
        # since it's always going to be 00
        return '00'
    elif num < 0:
        sign = "-"
        num = abs(num)

    # init both empty
    hex_nums, result = "", []
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while num != 0:
        # each new item to add to the hex string is
        # the remainder when you divide num by 16
        rem = num % 16
        new_val = hex_dict[rem] if rem in hex_dict.keys() else str(rem)
        hex_nums += new_val
        num = num // 16

    # split the string in to 2 byte sections (order needs to be
    # reversed since we generally read from the bottom when
    # taking the remainder doing this by hand
    [
        result.append(hex_nums[i:i + 2][::-1])
        for i in reversed(range(0, len(hex_nums), 2))
    ]

    if len(result[0]) < 2:
        result[0] = '0'+result[0]

    result = " ".join(result) if endian == "big" else " ".join(result[::-1])
    return sign + result
