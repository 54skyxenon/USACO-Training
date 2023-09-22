'''
ID: bwliang1
LANG: PYTHON3
TASK: milk4
'''

import sys
from itertools import combinations

PROBLEM_NAME = 'milk4'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

q = int(input())
p = int(input())

pails = []
for _ in range(p):
    pails.append(int(input()))
pails.sort()

def works(root, allowed, seen):
    if root == q:
        return True
    
    for pail_value in allowed:
        nei = root + pail_value
        if nei <= q and nei not in seen:
            seen.add(nei)
            if works(nei, allowed, seen):
                return True

    return False

for k in range(1, len(pails) + 1):
    for combo in combinations(pails, k):
        if works(0, combo, set([0])):
            print(len(combo), *combo)
            exit(0)