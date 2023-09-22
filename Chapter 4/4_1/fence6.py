'''
ID: bwliang1
LANG: PYTHON3
TASK: fence6
'''

import sys

PROBLEM_NAME = 'fence6'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

def readlist():
    return list(map(int, input().split()))

n = int(input())
left = [set() for _ in range(n)]
right = [set() for _ in range(n)]
cost = [0] * n

for _ in range(n):
    s, l, n1, n2 = readlist()
    cost[s - 1] = l
    left[s - 1].update([x - 1 for x in readlist()])
    right[s - 1].update([x - 1 for x in readlist()])

min_perimeter = float('inf')

def DFS(curr, parent, seen, perimeter):
    if curr in seen:
        global min_perimeter
        min_perimeter = min(min_perimeter, perimeter)
        return
    
    seen.add(curr)

    if parent not in left[curr]:
        for nei in left[curr]:
            DFS(nei, curr, seen, perimeter + cost[curr])

    if parent not in right[curr]:
        for nei in right[curr]:
            DFS(nei, curr, seen, perimeter + cost[curr])

    seen.discard(curr)

for i in range(n):
    DFS(i, -1, set(), 0)

print(min_perimeter)