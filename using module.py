# Calender Program

import calendar
import time
import platform


x = platform.system()
print(f"This is {x} platform", end="\n\n")

print("\t\t\t======| Your Calender |======\n")
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

my_calender = calendar.month(year, month)
print("\n", my_calender)

is_leap = calendar.isleap(year)
time.sleep(5)       # the next line (print()) will after 5 seconds
print(f"{year} is leap year?", is_leap, end="\n")

