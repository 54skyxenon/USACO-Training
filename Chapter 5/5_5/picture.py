'''
ID: bwliang1
LANG: PYTHON3
TASK: picture
'''

import sys
from itertools import accumulate

PROBLEM_NAME = 'picture'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

MAX_UNIQUE_POINTS = 2 * 5000

n = int(input())

# extreme coordinate bounds
min_x = min_y = float('inf')
max_x = max_y = float('-inf')

# coordinate index -> coordinate
conversion_x = [0] * MAX_UNIQUE_POINTS
conversion_y = [0] * MAX_UNIQUE_POINTS

# coordinate -> coordinate index
conversion_x_inv = dict()
conversion_y_inv = dict()

def get_perimeter():
    changes = [[] for _ in range(min_y + max_y + 1)]
    
    # for the bottom y and top y, add the starting and ending x-coordinate events
    for x1, y1, x2, y2 in rectangles:
        changes[y1 + min_y].append((x1, 1))
        changes[y1 + min_y].append((x2, -1))
        changes[y2 + min_y].append((x1, -1))
        changes[y2 + min_y].append((x2, 1))
    
    num_covered = [0] * (min_x + max_x + 1)
    perimeter = 0

    for y in range(min_y, max_y + 1):
        for x, dcnt in changes[y + min_y]:
            num_covered[x + min_x] += dcnt
        
        prev = 0
        for col_occupied in accumulate(num_covered):
            if (col_occupied > 0) ^ (prev > 0):
                perimeter += conversion_y[y + 1] - conversion_y[y]
            prev = col_occupied

    return perimeter

# Read all rectangles
rectangles = []
all_x = set()
all_y = set()

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    all_x.add(x1)
    all_x.add(x2)
    all_y.add(y1)
    all_y.add(y2)
    rectangles.append((x1, y1, x2, y2))

# Coordinate compress all rectangles
ix = 0
for x in sorted(all_x):
    conversion_x[ix] = x
    conversion_x_inv[x] = ix
    ix += 1

iy = 0
for y in sorted(all_y):
    conversion_y[iy] = y
    conversion_y_inv[y] = iy
    iy += 1

for i, (x1, y1, x2, y2) in enumerate(rectangles):
    rectangles[i] = (conversion_x_inv[x1], conversion_y_inv[y1], conversion_x_inv[x2], conversion_y_inv[y2])
    min_x = min(min_x, conversion_x_inv[x1])
    max_x = max(max_x, conversion_x_inv[x2])
    min_y = min(min_y, conversion_y_inv[y1])
    max_y = max(max_y, conversion_y_inv[y2])
    
# First get vertical perimeter
vertical = get_perimeter()

# Swap coordinates, then get horizontal perimeter
min_x, min_y, max_x, max_y = min_y, min_x, max_y, max_x
conversion_x, conversion_y = conversion_y, conversion_x
rectangles = [(y1, x1, y2, x2) for x1, y1, x2, y2 in rectangles]
horizontal = get_perimeter()

print(vertical + horizontal)