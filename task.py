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

    sign = ''
    if num < 0:
        sign = '-'
        num = abs(num)
    elif num == 0:
        # we do not need to convert to hex
        # since it's always going to be 00
        return '00'

    result = []
    hex_nums = dec_to_hex_string(num)

    # at this point hex_nums should be a continuous
    # string with no spaces in big endian direction
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
    if sign:
        result.append(sign)
    return " ".join(result)


def dec_to_hex_string(num):
    """
    Helper function for the conv_endian function. Takes a decimal value
    and converts it to a hex string
    :param num: decimal value
    :return: string hex value in big endian format
    """

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
    return hex_nums


if __name__ == '__main__':
    print(conv_endian(123))
    print(conv_endian(954786))
    print("zero", conv_endian(0))
    print(conv_endian(890))
