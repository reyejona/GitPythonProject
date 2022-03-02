"""
Names: Alyssa Comstock, Calvin Hoo
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
