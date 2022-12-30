#!/usr/bin/env python3
def is_leap(year):
    if (year%4==0 and year%400==0) or year%100!=0:
        return False
print(is_leap(1990))