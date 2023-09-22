'''
ID: bwliang1
LANG: PYTHON3
TASK: zerosum
'''

import sys
from itertools import product

PROBLEM_NAME = 'zerosum'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
symbols = [['+', '-', ' '] for _ in range(n - 1)]
ans = []

for ordered_set in product(*symbols):
    expr = list(' '.join(map(str, range(1, n + 1))))
    for i in range(1, len(expr), 2):
        expr[i] = str(ordered_set[(i - 1) // 2])
    
    expr = ''.join(expr)
    if eval(expr.replace(' ', '')) == 0:
        ans.append(expr)

for expr in sorted(ans):
    print(expr)