'''
ID: bwliang1
LANG: PYTHON3
TASK: comehome
'''

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

PROBLEM_NAME = 'comehome'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

graph = defaultdict(lambda: defaultdict(lambda: float('inf')))

def dijkstra():
    Q = [(0, 'Z')]
    heapify(Q)

    dist = defaultdict(lambda: float('inf'))
    dist['Z'] = 0

    while Q:
        d, u = heappop(Q)

        if d > dist[u]:
            continue

        for v, cost in graph[u].items():
            if d + cost < dist[v]:
                dist[v] = d + cost
                heappush(Q, (dist[v], v))

    ans_dist, ans_barn = min((d, barn) for barn, d in dist.items() if barn != 'Z' and barn.isupper())
    print(ans_barn, ans_dist)

p = int(input())
for _ in range(p):
    src, dest, cost = input().split()
    graph[src][dest] = graph[dest][src] = min(graph[dest][src], int(cost))

dijkstra()