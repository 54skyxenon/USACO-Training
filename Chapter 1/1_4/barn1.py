'''
ID: bwliang1
LANG: PYTHON3
TASK: barn1
'''

import sys
from functools import lru_cache

PROBLEM_NAME = 'barn1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

m, s, c = map(int, input().split())

stalls = []
for _ in range(c):
    stalls.append(int(input()))
stalls.sort()

if m >= c:
    print(c)
    exit(0)

@lru_cache(None)
def dp(i, remaining):
    if i == c - 1:
        return 1
    
    if remaining == 1:
        return stalls[-1] - stalls[i] + 1
    
    ans = float('inf')
    for j in range(i + 1, c):
        ans = min(ans, (stalls[j - 1] - stalls[i] + 1) + dp(j, remaining - 1))

    return ans

print(dp(0, m))