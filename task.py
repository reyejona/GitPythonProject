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
