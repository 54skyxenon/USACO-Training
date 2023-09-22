"""
ID: bwliang1
LANG: PYTHON3
TASK: hamming
"""

import sys

PROBLEM_NAME = 'hamming'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, b, d = map(int, input().split())

def hamming(s, t):
    s = '{0:b}'.format(s).zfill(b)
    t = '{0:b}'.format(t).zfill(b)
    return sum(a != b for a, b in zip(s, t))

def DFS(path):
    if len(path) == n:
        for i in range(0, len(path), 10):
            print(' '.join(map(str, path[i:i+10])))
        return True
    
    for nei in range(path[-1] + 1, 2 ** b):
        if all(hamming(p, nei) >= d for p in path):
            path.append(nei)
            if DFS(path):
                return True
            path.pop()

    return False

for i in range(2 ** b):
    if DFS([i]):
        break