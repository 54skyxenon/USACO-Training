'''
ID: bwliang1
LANG: PYTHON3
TASK: skidesign
'''

import sys

PROBLEM_NAME = 'skidesign'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

hills = []
for _ in range(n):
    hills.append(int(input()))
hills.sort()

ans = float('inf')
for smallest in range(hills[0], hills[-1] - 16):
    biggest = smallest + 17

    ans_here = 0
    for hill in hills:
        if hill < smallest:
            ans_here += (smallest - hill) ** 2
        
        if hill > biggest:
            ans_here += (hill - biggest) ** 2

    ans = min(ans, ans_here)

print(ans)