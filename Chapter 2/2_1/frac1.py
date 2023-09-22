"""
ID: bwliang1
LANG: PYTHON3
TASK: frac1
"""

import sys
from math import gcd

PROBLEM_NAME = 'frac1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

class Fraction:
    def __init__(self, numerator, denominator):
        frac_gcd = gcd(numerator, denominator)
        self.numerator = numerator // frac_gcd
        self.denominator = denominator // frac_gcd
    
    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

fractions = []

for i in range(1, n + 1):
    for j in range(i + 1):
        fractions.append(Fraction(j, i))

seen = set()
for f in sorted(fractions):
    if str(f) not in seen:
        seen.add(str(f))
        print(f)