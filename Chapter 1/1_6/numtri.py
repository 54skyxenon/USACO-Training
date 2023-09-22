"""
ID: bwliang1
LANG: PYTHON3
TASK: numtri
"""

import sys
from functools import lru_cache

sys.setrecursionlimit(150000)

PROBLEM_NAME = 'numtri'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

r = int(input())

triangle = []
for _ in range(r):
    triangle.append(list(map(int, input().split())))

@lru_cache(None)
def dp(i, j):
    if i == r - 1:
        return triangle[i][j]
    
    return triangle[i][j] + max(dp(i + 1, j), dp(i + 1, j + 1))

print(dp(0, 0))