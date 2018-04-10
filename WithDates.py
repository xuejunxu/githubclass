"""
A small script dealing with dates
"""

import datetime

def days_in_month(year,month):
    """
    Computing the number of days in a given month
    """

    if month==12:
        num_month=1
        num_year=year+1
    else:
        num_month=month+1
        num_year=year
    
    date_this_month=datetime.date(year,month,1)
    date_next_month=datetime.date(num_year,num_month,1)
    #Sububtracting the first of the given month from the first of the next month 
    #to get the number of days in the given month.
    
    diff_date=date_next_month-date_this_month
    return diff_date.days

#run some test of part 1
print(days_in_month(2017,2))
print("")
print(days_in_month(2015,7))

def is_valid_date(year, month, day):
    """
    Checking if a date is valid
    """

    if (datetime.MINYEAR<=year<=datetime.MAXYEAR) and (1<=month<=12) \
    and (1<=day<=days_in_month(year,month)):
        return True
    else:
        return False

#run some test of part 2
print("")
print("===========")
print("")
print(is_valid_date(2011,2,29))
print("")
print(is_valid_date(2022,3,31))


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if (is_valid_date(year1,month1,day1)) and (is_valid_date(year2,month2,day2)):
        date_first=datetime.date(year1,month1,day1)
        date_second=datetime.date(year2,month2,day2)
        if (date_second>=date_first):
            diff_days=date_second-date_first
            return int(diff_days.days)
        else:
            return 0
    else:
        return 0

#run some test of part 3
print("")
print("==========")
print("")
print(days_between(2013, 9, 1, 2017, 7, 1))
print("")
print(days_between(2013, 2, 29, 2017, 7, 1))
print("")
print(days_between(2018, 9, 1, 2017, 7, 1))


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    today_date=datetime.date.today()
    year1=year
    month1=month
    day1=day
    year2=int(today_date.year)
    month2=int(today_date.month)
    day2=int(today_date.day)
    if (days_between(year1, month1, day1, year2, month2, day2)==0):
        return 0
    else:
        return days_between(year1, month1, day1, year2, month2, day2)

#run some test

print("")
print("==========")
print(age_in_days(1994,11,19))
print("")
print(age_in_days(2005,2,31))
print("")
print(age_in_days(2022,1,1))