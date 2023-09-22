'''
ID: bwliang1
LANG: PYTHON3
TASK: fence3
'''

import sys

PROBLEM_NAME = 'fence3'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

f = int(input())

fences = []
for _ in range(f):
    x1, y1, x2, y2 = map(int, input().split())
    fences.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

def total_dist(source_x, source_y):
    ans = 0

    for min_x, min_y, max_x, max_y in fences:
        dx = max(0, min_x - source_x, source_x - max_x)
        dy = max(0, min_y - source_y, source_y - max_y)
        ans += (dx ** 2 + dy ** 2) ** 0.5
    
    return ans

x = y = 0
dx = dy = 20
optimum = total_dist(x, y)

# Can change moves from 50
for b in range(50):
    if b % 10 == 9:
        dx /= 10
        dy /= 10

    for nei_x, nei_y in [(x + dx, y), (x - dx, y), (x, y + dy), (x, y - dy)]:
        nei_dist = total_dist(nei_x, nei_y)
        if nei_dist < optimum:
            x, y = nei_x, nei_y
            optimum = nei_dist

print(f'{x:.1f} {y:.1f} {optimum:.1f}')

'''
# Disclaimer: simulated annealing is probabilistic and may need 20+ submissions for AC

import sys
import math
import random

PROBLEM_NAME = 'fence3'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

f = int(input())

lines = []
for _ in range(f):
    lines.append(tuple(map(int, input().split())))

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def dist_to_line(px, py, lx1, ly1, lx2, ly2):
    lx1, lx2 = min(lx1, lx2), max(lx1, lx2)
    ly1, ly2 = min(ly1, ly2), max(ly1, ly2)
    ans = min(dist(px, py, lx1, ly1), dist(px, py, lx2, ly2))

    # vertical
    if lx1 == lx2 and ly1 <= py <= ly2:
        ans = min(ans, abs(lx1 - px))
    
    # horizontal
    if ly1 == ly2 and lx1 <= px <= lx2:
        ans = min(ans, abs(ly1 - py))

    return ans

def sum_dist_to_lines(px, py):
    return sum(dist_to_line(px, py, *l) for l in lines)

def simulated_annealing_2d(f, x_min, x_max, y_min, y_max, T=500, T_min=0.01, alpha=0.8, iter_per_temp=50):
    # Initialize the solution to a random point within the given bounds.
    x_current = random.uniform(x_min, x_max)
    y_current = random.uniform(y_min, y_max)
    f_current = f(x_current, y_current)
    
    # Store the best solution found.
    x_best = x_current
    y_best = y_current
    f_best = f_current
    
    while T > T_min:
        for _ in range(iter_per_temp):
            # Generate a neighbor solution by taking a small random step.
            dx = random.uniform(-T, T) # step size can be adjusted
            dy = random.uniform(-T, T) # step size can be adjusted
            x_neighbor = x_current + dx
            y_neighbor = y_current + dy

            # Ensure new points are within the bounds.
            x_neighbor = max(x_min, min(x_neighbor, x_max))
            y_neighbor = max(y_min, min(y_neighbor, y_max))
            
            f_neighbor = f(x_neighbor, y_neighbor)
            
            # If the neighbor solution is better, or if we should probabilistically accept it.
            if f_neighbor < f_current or random.uniform(0, 1) < math.exp(-(f_neighbor - f_current) / T):
                x_current = x_neighbor
                y_current = y_neighbor
                f_current = f_neighbor

                # Update best solution if needed.
                if f_current < f_best:
                    x_best = x_current
                    y_best = y_current
                    f_best = f_current

        # Reduce the temperature.
        T *= alpha

    return x_best, y_best, f_best

lo_x = min(min(x1, x2) for x1, _, x2, _ in lines)
hi_x = max(max(x1, x2) for x1, _, x2, _ in lines)
lo_y = min(min(y1, y2) for _, y1, _, y2 in lines)
hi_y = max(max(y1, y2) for _, y1, _, y2 in lines)

x_best, y_best, f_best = simulated_annealing_2d(sum_dist_to_lines, lo_x, hi_x, lo_y, hi_y)
print(f'{x_best:.1f} {y_best:.1f} {f_best:.1f}')
'''