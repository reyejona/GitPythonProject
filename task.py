import re
"""
Names: Alyssa Comstock
Date:
Class: CS362 - Software Engineering II
Assignment: Group Project Part 2- Continuous Integration Workflow
Description:
"""

# this function will receive a string that can represent
# integers, floating point numbers and hexadecimals with prefix 0x
# and convert it to a base 10 number

def conv_num(num_str):
    # this function will receive a string representing a
    # floating point number or integer and convert it to a base 10 number
    def convert_int_float():
        decimal = 0
        # find if there is decimal in num_str
        for i in num_str:
            if i == '.':
                decimal += 1
        # If more than 1 decimal, it is rejected
        if decimal > 1:
            print("more than 1 decimal rejected")
            return None
        result_int_float = 0
        num = 0
        decimal_result = 0
        # if string with no decimal, is an integer
        if decimal == 0:
            # num_str should stay the same length
            num = num_str
        # if there is one decimal it is a floating type
        if decimal == 1:
            print("convert float")
            # find the '.' split integer part from decimal part
            num, dec_part = num_str.split('.')
            # convert the decimal component
            for digit in dec_part[::-1]:
                decimal_result /= 10
                for d in '0123456789':
                    decimal_result += digit > d
        # convert the integer part
        if decimal == 0 or decimal == 1:
            for digit in num:
                result_int_float *= 10
                for d in '0123456789':
                    result_int_float += digit > d
        # add the integer and decimal to get floating point number
        if decimal == 1:
            result_int_float = result_int_float + (decimal_result / 10)
            print(result_int_float)
        print(result_int_float)
        return result_int_float

    # this function will receive a string hex with 0x removed
    # and convert it to a decimal/integer value
    def convert_hex(x):
        print("convert hex")
        ret = 0
        # convert string lowercase into uppercase before converting to hex
        # enumerate will give 2 loop variables count (i), and index value (v)
        for i, v in enumerate(x.upper()):
            hexadecimal = "0123456789ABCDEF"  # hex values in index 0-15
            value = hexadecimal.index(v)  # value is decimal value equivalent of index
            power = (len(x) - (i + 1))  # power of hex equivalent
            ret += (value * 16 ** power)  # 16^power
            print(ret)
        return ret

    negative = False
    # check if not a string type or empty strings
    if type(num_str) != str or num_str == '':
        print("no string or empty")
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
            result = convert_hex(num_str)
        else:
            print("reject non hex characters")
            # if character is not Hex it will return none
            return None
    else:
        # use regex matching for finding valid integers and decimal
        # for floating point numbers
        valid_digits = re.compile("^[0-9\.]+$")
        # if valid integer or floating point number found, it is valid
        if valid_digits.match(num_str):
            result = convert_int_float()
        else:
            # if string is not numerical or a '.' it will return none
            print("string is not numerical or a '.'")
            return None
    if negative:
        # if negative, multiply by -1
        print("negative result")
        return result * - 1
    print(result)
    return result


def my_datetime(num_sec):
    pass


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
    print(conv_endian(-123))
