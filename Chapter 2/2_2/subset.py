"""
ID: bwliang1
LANG: PYTHON3
TASK: subset
"""

import sys
from functools import lru_cache

PROBLEM_NAME = 'subset'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

@lru_cache(None)
def dp(i, j):
    if j < 0:
        return 0
    
    if i == 0:
        return int(j == 0)

    return dp(i - 1, j - i) + dp(i - 1, j)

total = n * (n + 1) // 2
if total % 2 == 1:
    print(0)
else:
    print(dp(n, total // 2) // 2)