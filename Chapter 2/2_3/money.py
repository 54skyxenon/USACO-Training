'''
ID: bwliang1
LANG: PYTHON3
TASK: money
'''

import sys
from functools import cache

PROBLEM_NAME = 'money'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

all_input = list(sys.stdin.readlines())

v, n = map(int, all_input[0].split())
coins = []
for line in all_input[1:]:
    coins.extend(list(map(int, line.strip().split())))

@cache
def dp(i, j):
    if i == 0:
        return 1
    
    if i < 0 or j < 0:
        return 0

    return dp(i - coins[j], j) + dp(i, j - 1)

print(dp(n, v - 1))