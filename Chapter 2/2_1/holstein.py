"""
ID: bwliang1
LANG: PYTHON3
TASK: holstein
"""

import sys
from functools import reduce
from operator import add

PROBLEM_NAME = 'holstein'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

def readlist():
    return list(map(int, input().split()))

v = int(input())
requirements = readlist()

g = int(input())
feeds = []
for _ in range(g):
    feeds.append(readlist())

def feedsum(ss):
    return sum(sum(feeds[idx - 1]) for idx in ss)

powerset = reduce(lambda a, b: a + [ss + [b] for ss in a], range(1, g + 1), [[]])
powerset.sort(key=lambda ss: (len(ss), feedsum(ss)))
powerset.pop(0)

for subset in powerset:
    received = [0] * v
    for idx in subset:
        received = map(add, received, feeds[idx - 1])

    if all(have >= need for have, need in zip(received, requirements)):
        print(len(subset), end=' ')
        print(' '.join(map(str, subset)))
        break