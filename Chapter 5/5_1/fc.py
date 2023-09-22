'''
ID: bwliang1
LANG: PYTHON3
TASK: fc
'''

import sys

PROBLEM_NAME = 'fc'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append(Point2D(x, y))

def convex_hull():
    ''' https://leetcode.com/problems/erect-the-fence/solutions/103300/Detailed-explanation-of-Graham-scan-in-14-lines-(Python)/ '''
    # Computes the cross product of vectors p1p2 and p2p3 value
    # = 0 means points are colinear
    # < 0 means cw
    # > 0 means ccw
    def cross(p1, p2, p3):
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    # Computes slope of line between p1 and p2
    def slope(p1, p2):
        dy, dx = p1.y - p2.y, p1.x - p2.x
        return dy / dx if dx != 0 else float('inf')

    # Find the smallest left point and remove it from points
    start = min(points, key=lambda p: (p.x, p.y))
    points.pop(points.index(start))

    # Sort points so that traversal is from start in a ccw circle
    points.sort(key=lambda p: slope(p, start))

    # Add each point to the convex hull.
    # If the last 3 points make a cw turn, the second to last point is wrong. 
    ans = [start]
    for p in points:
        ans.append(p)
        while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
            ans.pop(-2)
    
    return ans

hull = convex_hull()
ans = sum(hull[i - 1].dist(hull[i]) for i in range(len(hull)))
print('{:.2f}'.format(ans))