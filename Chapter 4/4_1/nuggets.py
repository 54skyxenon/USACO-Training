'''
ID: bwliang1
LANG: PYTHON3
TASK: nuggets
'''

import sys
from functools import cache

PROBLEM_NAME = 'nuggets'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

packages = []
for _ in range(n):
    packages.append(int(input()))

@cache
def dp(i):
    if i < 0:
        return False
    
    if i == 0:
        return True
    
    return any(dp(i - p) for p in packages)

largest = max(packages)
seen = set()
ans = multiple = 0

while True:
    possible = [int(dp(i)) for i in range(multiple, multiple + largest)]

    if all(possible):
        break
    else:
        ans = max([i for i in range(multiple, multiple + largest) if not dp(i)])

    state = ''.join(map(str, possible))
    if state in seen:
        print(0)
        exit(0)
    else:
        seen.add(state)

    multiple += largest

print(ans)