'''
ID: bwliang1
LANG: PYTHON3
TASK: runround
'''

import sys

PROBLEM_NAME = 'runround'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

m = int(input())

def is_runaround(x):
    x = str(x)
    if '0' in x or len(set(x)) != len(x):
        return False

    i = 0
    seen = set()

    while True:
        if i in seen:
            break
        else:
            seen.add(i)
            i = (i + int(x[i])) % len(x)

    return len(seen) == len(x) and i == 0

x = m + 1
while not is_runaround(x):
    x += 1

print(x)