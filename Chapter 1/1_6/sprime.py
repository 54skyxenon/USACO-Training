"""
ID: bwliang1
LANG: PYTHON3
TASK: sprime
"""

import sys

PROBLEM_NAME = 'sprime'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

candidates = [['2', '3', '5', '7']]
for _ in range(n - 1):
    candidates.append(['1', '3', '5', '7', '9'])

def is_prime(path):
    num = int(''.join(path))

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

ans = []
def DFS(path, index):
    if index == n:
        ans.append(''.join(path))
        return

    for c in candidates[index]:
        path.append(c)
        if is_prime(path):
            DFS(path, index + 1)
        path.pop()

DFS([], 0)
for a in sorted(ans):
    print(a)