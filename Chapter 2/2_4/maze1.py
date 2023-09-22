'''
ID: bwliang1
LANG: PYTHON3
TASK: maze1
'''

import sys
from collections import deque

PROBLEM_NAME = 'maze1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

w, h = map(int, input().split())

grid = []
for _ in range(2 * h + 1):
    grid.append(input())

dist = dict()
Q = deque()

for col in range(len(grid[0])):
    if grid[0][col] == ' ':
        dist[(1, col)] = 1
        Q.append(((1, col), 1))

    if grid[-1][col] == ' ':
        dist[(len(grid) - 2, col)] = 1
        Q.append(((len(grid) - 2, col), 1))

for row in range(len(grid)):
    if grid[row][0] == ' ':
        dist[(row, 1)] = 1
        Q.append(((row, 1), 1))

    if grid[row][-1] == ' ':
        dist[(row, len(grid[0]) - 2)] = 1
        Q.append(((row, len(grid[0]) - 2), 1))

while Q:
    (r, c), depth = Q.popleft()

    for nr, nc in [(r + 2, c), (r - 2, c), (r, c + 2), (r, c - 2)]:
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            between_r = (r + nr) // 2
            between_c = (c + nc) // 2
            if grid[between_r][between_c] not in {'|', '-', '+'} and grid[nr][nc] == ' ' and (nr, nc) not in dist:
                dist[(nr, nc)] = depth + 1
                Q.append(((nr, nc), depth + 1))

print(max(dist.values()))