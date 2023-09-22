'''
ID: bwliang1
LANG: PYTHON3
TASK: friday
'''

import sys

PROBLEM_NAME = 'friday'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans = [0] * 7
day_index = 2

n = int(input())

def is_leap_year(year):
    if year in {1900, 2100, 2200, 2300}:
        return False
    
    if year == 2000:
        return True
    
    return year % 4 == 0

for year in range(1900, 1900 + n):
    for month in (months_leap if is_leap_year(year) else months):
        ans[(day_index + 12) % 7] += 1
        day_index = (day_index + month) % 7

print(' '.join(map(str, ans)))