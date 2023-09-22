'''
ID: bwliang1
LANG: PYTHON3
TASK: tour
'''

import sys
from functools import cache
from collections import defaultdict
from itertools import product

PROBLEM_NAME = 'tour'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, v = map(int, input().split())

cities = []
for _ in range(n):
    cities.append(input())
city_index = dict((c, i) for i, c in enumerate(cities))

east_of = defaultdict(set)
for _ in range(v):
    src, dest = input().split()
    if city_index[dest] > city_index[src]:
        east_of[src].add(dest)
    else:
        east_of[dest].add(src)

@cache
def dp(i, j):
    ''' INVARIANT: `j` is not west of `i` for simplicity's sake.
        Counts nodes going east from i to the end, then west from the end to j.
    '''
    if city_index[i] > city_index[j]:
        return dp(j, i)

    ans = float('-inf')
    frontier = max(city_index[i], city_index[j])

    for east_i, east_j in product(east_of[i], east_of[j]):
        if city_index[east_i] > frontier:
            ans = max(ans, 1 + dp(east_i, j))

        if city_index[east_j] > frontier:
            ans = max(ans, 1 + dp(i, east_j))

        if min(city_index[east_i], city_index[east_j]) > frontier:
            if east_i == east_j == cities[-1]:
                ans = max(ans, 3)
            
            if city_index[east_j] > city_index[east_i]:
                ans = max(ans, 2 + dp(east_i, east_j))

    return ans

ans = dp(cities[0], cities[0]) - 1
print(ans if ans > float('-inf') else 1)