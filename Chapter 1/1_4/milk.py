'''
ID: bwliang1
LANG: PYTHON3
TASK: milk
'''

import sys

PROBLEM_NAME = 'milk'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, m = map(int, input().split())

farmers = []
for _ in range(m):
    p, a = map(int, input().split())
    farmers.append((p, a))
farmers.sort()

bought = spent = 0

for p, a in sorted(farmers):
    bought_here = min(n - bought, a)
    bought += bought_here
    spent += bought_here * p
    
print(spent)