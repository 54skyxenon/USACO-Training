'''
ID: bwliang1
LANG: PYTHON3
TASK: snail
'''

import sys
from itertools import product

PROBLEM_NAME = 'snail'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, b = map(int, input().split())
grid = [['.'] * n for _ in range(n)]

for _ in range(b):
    cell = input()
    c, r = cell[:1], cell[1:]
    grid[int(r) - 1][ord(c) - ord('A')] = '#'

ans = 1
graph = [[dict() for _ in range(n)] for _ in range(n)]

def add_edges(r, c):
    if grid[r][c] == '#':
        return

    # North
    top_r = r
    for nr in range(r - 1, -1, -1):
        if grid[nr][c] == '#':
            break
        top_r -= 1

    if (top_r, c) != (r, c):
        graph[r][c]['N'] = (top_r, c)

    # South
    bottom_r = r
    for nr in range(r + 1, n):
        if grid[nr][c] == '#':
            break
        bottom_r += 1

    if (bottom_r, c) != (r, c):
        graph[r][c]['S'] = (bottom_r, c)

    # West
    left_c = c
    for nc in range(c - 1, -1, -1):
        if grid[r][nc] == '#':
            break
        left_c -= 1

    if (r, left_c) != (r, c):
        graph[r][c]['W'] = (r, left_c)

    # East
    right_c = c
    for nc in range(c + 1, n):
        if grid[r][nc] == '#':
            break
        right_c += 1

    if (r, right_c) != (r, c):
        graph[r][c]['E'] = (r, right_c)

def DFS(r, c, visited):
    global ans

    for d, (nr, nc) in graph[r][c].items():
        if d == 'N':
            # fill from [nr, r)
            for ir in range(r - 1, nr - 1, -1):
                if grid[ir][c] == 'x':
                    for ir_rev in range(ir + 1, r):
                        visited -= 1
                        grid[ir_rev][c] = '.'
                    break
                else:
                    grid[ir][c] = 'x'
                    visited += 1
                    ans = max(ans, visited)
                    if ir == nr:
                        DFS(nr, nc, visited)
                        for ir_rev in range(nr, r):
                            visited -= 1
                            grid[ir_rev][c] = '.'
        elif d == 'S':
            # fill from (r, nr]
            for ir in range(r + 1, nr + 1):
                if grid[ir][c] == 'x':
                    for ir_rev in range(ir - 1, r, -1):
                        visited -= 1
                        grid[ir_rev][c] = '.'
                    break
                else:
                    grid[ir][c] = 'x'
                    visited += 1
                    ans = max(ans, visited)
                    if ir == nr:
                        DFS(nr, nc, visited)
                        for ir_rev in range(r + 1, nr + 1):
                            visited -= 1
                            grid[ir_rev][c] = '.'
        elif d == 'W':
            # fill from [nc, c)
            for ic in range(c - 1, nc - 1, -1):
                if grid[r][ic] == 'x':
                    for ic_rev in range(ic + 1, c):
                        visited -= 1
                        grid[r][ic_rev] = '.'
                    break
                else:
                    grid[r][ic] = 'x'
                    visited += 1
                    ans = max(ans, visited)
                    if ic == nc:
                        DFS(nr, nc, visited)
                        for ic_rev in range(nc, c):
                            visited -= 1
                            grid[r][ic_rev] = '.'
        elif d == 'E':
            # fill from (c, nc]
            for ic in range(c + 1, nc + 1):
                if grid[r][ic] == 'x':
                    for ic_rev in range(ic - 1, c, -1):
                        visited -= 1
                        grid[r][ic_rev] = '.'
                    break
                else:
                    grid[r][ic] = 'x'
                    visited += 1
                    ans = max(ans, visited)
                    if ic == nc:
                        DFS(nr, nc, visited)
                        for ic_rev in range(c + 1, nc + 1):
                            visited -= 1
                            grid[r][ic_rev] = '.'

for cell in product(range(n), range(n)):
    add_edges(*cell)

grid[0][0] = 'x'
DFS(0, 0, 1)
print(ans)