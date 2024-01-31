def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """ Checks if the year is a leap year
        return the number of days in the month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
    if is_leap(year):
        return 29
    return month_days[month + 1]
    
year = int(input("Please enter Year: "))
month = int(input("Please enter Month: "))

check = days_in_month(year=2024, month=2)
print(check)