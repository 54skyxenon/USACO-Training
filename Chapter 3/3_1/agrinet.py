'''
ID: bwliang1
LANG: PYTHON3
TASK: agrinet
'''

import sys

PROBLEM_NAME = 'agrinet'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

graph = list(sys.stdin.readlines())
graph = list(map(int, ' '.join(graph).split()))
graph = [graph[i:i + n] for i in range(0, n ** 2, n)]

included = set([0])
cost = 0

while len(included) < n:
    d, closest = min(sum([[(graph[i][j], j) for j in range(n) if j not in included] for i in included], []))
    cost += d
    included.add(closest)

print(cost)