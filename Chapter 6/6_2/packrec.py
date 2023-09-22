'''
ID: bwliang1
LANG: PYTHON3
TASK: packrec
'''

import sys
from collections import defaultdict
from itertools import product, permutations

PROBLEM_NAME = 'packrec'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

areas = defaultdict(set)

def add_area(width, height):
    area = width * height
    p, q = min(width, height), max(width, height)
    areas[area].add((p, q))

def get_rotations(rect):
    if rect[0] == rect[1]:
        return [rect]

    return [rect, rect[::-1]]

rects = []
for _ in range(4):
    rects.append(tuple(map(int, input().split())))

def valid_layout_6(x_limit, y_limit, *sq):
    for i in range(len(sq) - 1):
        for j in range(i + 1, len(sq)):
            y_start_1, y_end_1, x_start_1, x_end_1 = sq[i]
            y_start_2, y_end_2, x_start_2, x_end_2 = sq[j]

            # Check out of bounds
            if max(y_end_1, y_end_2) > y_limit or max(x_end_1, x_end_2) > x_limit:
                return False
            
            # Check if area ranges intersect
            if max(y_start_1, y_start_2) < min(y_end_1, y_end_2) and max(x_start_1, x_start_2) < min(x_end_1, x_end_2):
                return False
    
    return True

for p in permutations(rects):
    for (x1, y1), (x2, y2), (x3, y3), (x4, y4) in product(*map(get_rotations, p)):
        # Layout 1
        add_area(x1 + x2 + x3 + x4, max(y1, y2, y3, y4))

        # Layout 2
        add_area(max(x1 + x2 + x3, x4), max(y1, y2, y3) + y4)

        # Layout 3
        add_area(max(x1 + x2, x3) + x4, max(y4, y3 + max(y1, y2)))

        # Layout 4
        add_area(x1 + max(x2, x3) + x4, max(y1, y2 + y3, y4))

        # Layout 5
        add_area(max(x1, x2) + x3 + x4, max(y1 + y2, y3, y4))

        # Layout 6 (is the hardest of all of them to deal with)
        sq1 = (0, y1, 0, x1)
        sq2 = (y1, y1 + y3, 0, x3)
        sq3 = (0, y2, x1, x1 + x2)
        sq4 = (y2, y2 + y4, x1 + x2 - x4, x1 + x2)
        if valid_layout_6(x1 + x2, y1 + y3, sq1, sq2, sq3, sq4):
            add_area(y1 + y3, x1 + x2)

best_area = min(areas)
print(best_area)
for p, q in sorted(areas[best_area]):
    print(p, q)