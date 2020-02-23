def is_leap_year(year):
    """
    Is the given year a leap year?
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def calc_year(days):
    """
    Take in number of days since jan 1, 1980, and return the current year.
    """
    year = 1980;

    while days > 365:
        if is_leap_year(year):
            if days > 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1

    return year
