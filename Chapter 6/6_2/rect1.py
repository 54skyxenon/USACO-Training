'''
ID: bwliang1
LANG: PYTHON3
TASK: rect1
'''

import sys
from functools import reduce
from collections import defaultdict

PROBLEM_NAME = 'rect1'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

a, b, n = map(int, input().split())

def split_off(initial, affected):
    x11, y11, x21, y21, c1 = initial
    x12, y12, x22, y22, c2 = affected

    intersection = (max(x11, x12), max(y11, y12), min(x21, x22), min(y21, y22))

    # nothing in common
    if intersection[0] >= intersection[2] or intersection[1] >= intersection[3]:
        return [initial]
    
    new_rectangles = []

    # carve out top
    if intersection[3] < initial[3]:
        new_rectangles.append((initial[0], intersection[3], initial[2], initial[3], c1))
        
    # carve out bottom
    if intersection[1] > initial[1]:
        new_rectangles.append((initial[0], initial[1], initial[2], intersection[1], c1))
    
    # carve out left
    if intersection[0] > initial[0]:
        new_rectangles.append((initial[0], intersection[1], intersection[0], intersection[3], c1))

    # carve out right
    if intersection[2] < initial[2]:
        new_rectangles.append((intersection[2], intersection[1], initial[2], intersection[3], c1))

    return new_rectangles

rectangles = []
for _ in range(n):
    llx, lly, urx, ury, color = map(int, input().split())
    rectangles.append((llx, lly, urx, ury, color))
rectangles = reduce(lambda a, b: sum([split_off(r, b) for r in a], []) + [b], rectangles, [[0, 0, a, b, 1]])

areas = defaultdict(int)

for llx, lly, urx, ury, color in rectangles:
    areas[color] += (urx - llx) * (ury - lly)

for color in range(1, 2501):
    if areas[color] > 0:
        print(color, areas[color])