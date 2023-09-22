"""
ID: bwliang1
LANG: PYTHON3
TASK: ride
"""

import sys
from operator import mul
from functools import reduce

PROBLEM_NAME = 'ride'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

comet = input()
group = input()

final_comet = reduce(mul, [ord(c) - ord('A') + 1 for c in comet], 1)
final_group = reduce(mul, [ord(c) - ord('A') + 1 for c in group], 1)

print('GO' if (final_comet - final_group) % 47 == 0 else 'STAY')