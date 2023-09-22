'''
ID: bwliang1
LANG: PYTHON3
TASK: concom
'''

import sys
from collections import deque, defaultdict

PROBLEM_NAME = 'concom'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

Q = deque()
ownership = defaultdict(lambda: defaultdict(int))

for _ in range(n):
    i, j, p = map(int, input().split())
    ownership[i][j] += p
    if p > 50:
        Q.append((i, j))

ans = set()

while Q:
    src, dest = Q.popleft()

    if (src, dest) not in ans:
        ans.add((src, dest))
        for nei in ownership[dest]:
            ownership[src][nei] += ownership[dest][nei]
            if ownership[src][nei] > 50:
                Q.append((src, nei))

for a, b in sorted(ans):
    if a != b:
        print(a, b)