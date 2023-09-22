'''
ID: bwliang1
LANG: PYTHON3
TASK: palsquare
'''

import sys
import string

PROBLEM_NAME = 'palsquare'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

b = int(input())

def change_base(n):
    e, q = divmod(n, b)
    q_rep = str(q) if q < 10 else string.ascii_uppercase[q - 10]
    if n == 0:
        return '0'
    elif e == 0:
        return q_rep
    else:
        return change_base(e) + q_rep
    
for i in range(1, 301):
    if change_base(i ** 2) == change_base(i ** 2)[::-1]:
        print(change_base(i), change_base(i ** 2))