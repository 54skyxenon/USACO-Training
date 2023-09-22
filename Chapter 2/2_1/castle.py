"""
ID: bwliang1
LANG: PYTHON3
TASK: castle
"""

import sys
from itertools import product

PROBLEM_NAME = 'castle'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

m, n = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def adj(i, j):
    bitset = '{0:b}'.format(grid[i][j]).zfill(4)
    adj_list = []

    if bitset[0] == '0':
        adj_list.append((i + 1, j))

    if bitset[1] == '0':
        adj_list.append((i, j + 1))

    if bitset[2] == '0':
        adj_list.append((i - 1, j))

    if bitset[3] == '0':
        adj_list.append((i, j - 1))

    return adj_list

def get_ccs():
    cc = []
    cc_ids = dict()
    unvisited = set((i, j) for i, j in product(range(n), range(m)))

    def DFS(curr, seen):
        for nei in adj(*curr):
            if nei in unvisited:
                unvisited.remove(nei)
                seen.add(nei)
                DFS(nei, seen)

    cid = 0

    for i in range(n):
        for j in range(m):
            if (i, j) in unvisited:
                seen = set([(i, j)])
                unvisited.remove((i, j))
                DFS((i, j), seen)
                for ci, cj in seen:
                    cc_ids[(ci, cj)] = cid
                cc.append(seen)
                cid += 1

    return cc, cc_ids

cc, cc_ids = get_ccs()
print(len(cc))
best = max(len(cc_nodes) for cc_nodes in cc)
print(best)

best = float('-inf')
ans = ''

for remove_j in range(m):
    for remove_i in range(n - 1, -1, -1):
        if remove_i > 0 and grid[remove_i][remove_j] & 2: # remove north wall
            c1_id = cc_ids[(remove_i, remove_j)]
            c2_id = cc_ids[(remove_i - 1, remove_j)]
            candidate = len(cc[c1_id]) + len(cc[c2_id]) if c1_id != c2_id else len(cc[c2_id])
            if candidate > best:
                ans = f'{remove_i + 1} {remove_j + 1} N'
                best = candidate

        if remove_j < m - 1 and grid[remove_i][remove_j] & 4: # remove east wall
            c1_id = cc_ids[(remove_i, remove_j)]
            c2_id = cc_ids[(remove_i, remove_j + 1)]
            candidate = len(cc[c1_id]) + len(cc[c2_id]) if c1_id != c2_id else len(cc[c2_id])
            if candidate > best:
                ans = f'{remove_i + 1} {remove_j + 1} E'
                best = candidate

print(best)
print(ans)