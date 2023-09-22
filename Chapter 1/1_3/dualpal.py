'''
ID: bwliang1
LANG: PYTHON3
TASK: dualpal
'''

import sys

PROBLEM_NAME = 'dualpal'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, s = map(int, input().split())

def change_base(n, b):
    e, q = divmod(n, b)
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return change_base(e, b) + str(q)

def works(x):
    num_palindromic = 0
    for b in range(2, 11):
        num_palindromic += change_base(x, b) == change_base(x, b)[::-1]
        if num_palindromic >= 2:
            return True
    return False

x = s + 1
satisfied = 0

while satisfied < n:
    if works(x):
        print(x)
        satisfied += 1
    x += 1