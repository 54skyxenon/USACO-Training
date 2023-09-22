'''
ID: bwliang1
LANG: PYTHON3
TASK: ttwo
'''

import sys
from itertools import product

PROBLEM_NAME = 'ttwo'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

grid = []
for _ in range(10):
    grid.append(input())

clockwise = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}
adj = {
    'N': lambda r, c: (r - 1, c),
    'E': lambda r, c: (r, c + 1),
    'S': lambda r, c: (r + 1, c),
    'W': lambda r, c: (r, c - 1)
}

def encode(r, c):
    return 10 * r + c

def advance(posn, direction):
    nr, nc = adj[direction](*posn)

    if 0 <= nr < 10 and 0 <= nc < 10 and grid[nr][nc] != '*':
        return (nr, nc), direction
    else:
        return posn, clockwise[direction]
    
def solve():
    current_fj_posn = None
    current_fj_direction = 'N'
    current_cows_posn = None
    current_cows_direction = 'N'

    for i, j in product(range(10), range(10)):
        if grid[i][j] == 'C':
            current_cows_posn = (i, j)

        if grid[i][j] == 'F':
            current_fj_posn = (i, j)
    
    seen = set()
    steps = 0

    while True:
        if current_fj_posn == current_cows_posn:
            return steps

        curr_state = (encode(*current_fj_posn), current_fj_direction, encode(*current_cows_posn), current_cows_direction)
        if curr_state in seen:
            break
        seen.add(curr_state)

        current_fj_posn, current_fj_direction = advance(current_fj_posn, current_fj_direction)
        current_cows_posn, current_cows_direction = advance(current_cows_posn, current_cows_direction)
        steps += 1

    return 0

print(solve())