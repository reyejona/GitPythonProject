"""
Names:
Date:
Class: CS362 - Software Engineering II
Assignment:
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
        # before anything is calculated
        return None

    temp = num
    hex_nums = ''
    result = []
    hex_dict = {
        0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    
    while temp != 0:
        # Calculate the value first, and the direction will be
        # reversed based on what endian direction it is
        hex_nums += str(hex_dict[temp % 16])
        temp = temp//16
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
    return " ".join(result)


if __name__ == '__main__':
    print(conv_endian(123))
    print(conv_endian(954786))
