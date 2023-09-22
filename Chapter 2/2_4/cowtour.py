'''
ID: bwliang1
LANG: PYTHON3
TASK: cowtour
'''

# NOTE: Has a 50% chance of AC since Python is slow (so keep submitting!)

import sys
from itertools import product

PROBLEM_NAME = 'cowtour'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

location = []
for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

def path_dist(l1, l2):
    x1, y1 = location[l1]
    x2, y2 = location[l2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

graph = [set() for _ in range(n)]
for i in range(n):
    graph[i].update(set(j for j, c in enumerate(input()) if c == '1'))

# Start with all single edge paths.
fw_dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    fw_dist[i][i] = 0
    for j in graph[i]:
        fw_dist[i][j] = path_dist(i, j)

# k is the 'intermediate' vertex
for k in range(n):
    for i in range(n):
        for j in range(n):
            if fw_dist[i][k] + fw_dist[k][j] < fw_dist[i][j]:
                fw_dist[i][j] = fw_dist[i][k] + fw_dist[k][j]

seen = [False] * n
def DFS(curr, cc):
    for nei in graph[curr]:
        if not seen[nei]:
            seen[nei] = True
            cc.add(nei)
            DFS(nei, cc)

fields = []
for i in range(n):
    if not seen[i]:
        seen[i] = True
        cc = set([i])
        DFS(i, cc)
        fields.append(cc)

max_valid = []
for i in range(n):
    max_valid.append(max(d for d in fw_dist[i] if d < float('inf')))

ans = float('inf')
for i in range(len(fields) - 1):
    for j in range(i + 1, len(fields)):
        max_field_diameter = max(max_valid[p] for p in fields[i] | fields[j])
        for p1, p2 in product(fields[i], fields[j]):
            ans = min(ans, max(path_dist(p1, p2) + max_valid[p1] + max_valid[p2], max_field_diameter))

print('{0:3f}'.format(ans))