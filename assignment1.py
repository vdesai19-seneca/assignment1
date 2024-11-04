#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Vivek Desai
Semester: Fall2024
Description: Assignment 1 C
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))               # Split date and convert to integers
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']           # List of days starting from Sunday
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}  # Month offsets
    if month < 3:
        year -= 1                                                      # Adjust year if month is Jan or Feb
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7  # Calculate day index
    return days[num]                                                   # Return corresponding day name

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    lyear = year % 4
    leap_flag = lyear == 0                                             # Check if year is divisible by 4
    lyear = year % 100
    if lyear == 0:
        leap_flag = False                                              # If divisible by 100, not a leap year
    lyear = year % 400
    if lyear == 0:
        leap_flag = True                                               # If divisible by 400, is a leap year
    return leap_flag 

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month, including leap year adjustment"
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,              # Standard max days in each month
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):                                 # February in leap year has 29 days
        return 29
    return mon_dict[month]

def after(date: str) -> str: 
    "Returns the next day's date in DD/MM/YYYY format"
    day, mon, year = (int(x) for x in date.split('/'))                 # Split date into day, month, year
    day += 1                                                           # Move to the next day
    if day > mon_max(mon, year):                                       # Reset to 1 if day exceeds month's max
        day = 1
        mon += 1                                                       # Move to next month
        if mon > 12:                                                   # Reset month to January if exceeds December
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"                                 # Return date in DD/MM/YYYY format

def before(date: str) -> str:
    "Returns the previous day's date in DD/MM/YYYY format"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1                                                           # Move to the previous day
    if day < 1:                                                        # If day goes below 1, adjust month
        mon -= 1
        if mon < 1:                                                    # If month goes below 1, adjust year and month
            mon = 12
            year -= 1
        day = mon_max(mon, year)                                       # Set day to max of previous month
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY ##")             # Print usage instruction
    sys.exit()                                                         # Exit the program

def valid_date(date: str) -> bool:
    "Check validity of a date in DD/MM/YYYY format"
    if len(date) != 10:                                                # Ensure date is in DD/MM/YYYY format
        return False
    try:
        day, month, year = map(int, date.split('/'))                   # Convert date components to integers
        return 1 <= month <= 12 and 1 <= day <= mon_max(month, year)   # Check valid day and month
    except ValueError:
        return False                                                   # Return False if conversion fails

def day_iter(start_date: str, num: int) -> str:
    "Iterates from start_date by num days to return end date in DD/MM/YYYY format"
    iter_date = start_date
    while num > 0:                                                     # Move forward in days
        iter_date = after(iter_date)
        num -= 1
    while num < 0:                                                     # Move backward in days
        iter_date = before(iter_date)
        num += 1
    return iter_date

if __name__ == "__main__":
    if len(sys.argv) != 3:                                             # Check if two arguments are passed
        usage()

    start_date = sys.argv[1]
    if not valid_date(start_date):                                     # Validate start date format
        usage()

    try:
        num = int(sys.argv[2])                                         # Ensure second argument is an integer
    except ValueError:
        usage()

    end_date = day_iter(start_date, num)                               # Calculate end date after iterations
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')     # Output end date with day of the week
