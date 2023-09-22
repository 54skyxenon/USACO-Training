'''
ID: bwliang1
LANG: PYTHON3
TASK: starry
'''

import sys
from itertools import product
from collections import defaultdict
from copy import deepcopy

PROBLEM_NAME = 'starry'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

w = int(input())
h = int(input())

sky = []
for _ in range(h):
    sky.append(list(input()))

num_clusters = 0
cluster_of_cell = dict()
cluster = defaultdict(set)

def DFS(r, c):
    for dy, dx in product([-1, 0, 1], [-1, 0, 1]):
        nr = r + dy
        nc = c + dx
        if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in cluster_of_cell and sky[nr][nc] == '1':
            cluster_of_cell[(nr, nc)] = num_clusters
            cluster[num_clusters].add((nr, nc))
            DFS(nr, nc)

for r, c in product(range(h), range(w)):
    if sky[r][c] == '1' and (r, c) not in cluster_of_cell:
        cluster_of_cell[(r, c)] = num_clusters
        cluster[num_clusters].add((r, c))
        DFS(r, c)
        num_clusters += 1

def get_subgrid(cluster_data):
    lower_r = lower_c = float('inf')
    upper_r = upper_c = float('-inf')
    
    for r, c in cluster_data:
        lower_r = min(lower_r, r)
        lower_c = min(lower_c, c)
        upper_r = max(upper_r, r)
        upper_c = max(upper_c, c)

    subgrid = []
    for r in range(lower_r, upper_r + 1):
        row = []
        for c in range(lower_c, upper_c + 1):
            if (r, c) in cluster_data:
                row.append('1')
            else:
                row.append('0')
        subgrid.append(row)

    return subgrid

def reflect(grid):
    reflected = deepcopy(grid)
    for row in reflected:
        l, r = 0, len(row) - 1
        while l < r:
            row[l], row[r] = row[r], row[l]
            l += 1
            r -= 1
    return reflected

def rotate(grid):
    return list(map(list, zip(*grid[::-1])))

def are_similar(subgrid_1, subgrid_2):
    original = subgrid_2
    once = rotate(original)
    twice = rotate(once)
    thrice = rotate(twice)
    return any(subgrid_1 == rotation or subgrid_1 == reflect(rotation) for rotation in [original, once, twice, thrice])

letter_of_cluster = [None] * len(cluster)
subgrids = [get_subgrid(cluster[i]) for i in range(num_clusters)]
best_letter = 'a'

for cluster_id in range(num_clusters):
    if letter_of_cluster[cluster_id] is None:
        letter_of_cluster[cluster_id] = best_letter

        for j in range(cluster_id + 1, num_clusters):
            if letter_of_cluster[j] is None and are_similar(subgrids[cluster_id], subgrids[j]):
                letter_of_cluster[j] = best_letter

        best_letter = chr(ord(best_letter) + 1)

output = [['0'] * w for _ in range(h)]
for r, c in product(range(h), range(w)):
    if sky[r][c] == '1':
        output[r][c] = letter_of_cluster[cluster_of_cell[(r, c)]]

for row in output:
    print(''.join(row))