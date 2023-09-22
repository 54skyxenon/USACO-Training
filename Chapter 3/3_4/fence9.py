'''
ID: bwliang1
LANG: PYTHON3
TASK: fence9
'''

import sys
from math import gcd
from fractions import Fraction

PROBLEM_NAME = 'fence9'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, m, p = map(int, input().split())

# Apply Pick's Theorem
area = Fraction(p * m, 2)
b = p + gcd(m, n) + gcd(m, abs(p - n))
i = area + 1 - Fraction(b, 2)
print(i)