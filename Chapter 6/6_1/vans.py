'''
ID: bwliang1
LANG: PYTHON3
TASK: vans
'''

import sys

PROBLEM_NAME = 'vans'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

# I feel like searching https://oeis.org/ for the base cases is cheating, but I'm lazy :D
dp = [0, 1, 2, 6]
for i in range(4, n):
    dp.append(2 * dp[-1] + 2 * dp[-2] - 2 * dp[-3] + dp[-4])

print(2 * dp[n - 1])