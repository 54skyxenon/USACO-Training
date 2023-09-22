'''
ID: bwliang1
LANG: PYTHON3
TASK: telecow
'''

import sys
from collections import defaultdict

PROBLEM_NAME = 'telecow'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

N, M, c1, c2 = map(int, input().split())
graph = dict()

# Add inner edges
for i in range(N):
    graph[f'{i}A'] = defaultdict(int)
    graph[f'{i}B'] = defaultdict(int)
    graph[f'{i}A'][f'{i}B'] = 2 ** N - 2 ** (N - 1 - i)

# Add original edges
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    graph[f'{u}B'][f'{v}A'] = float('inf')
    graph[f'{v}B'][f'{u}A'] = float('inf')

def ford_fulkerson(src, sink):
    total_flow = 0
    
    while True:
        # find path with highest capacity from src to sink, using modified Dijkstra's
        prev = dict()
        visited = set()
        flow = defaultdict(int, {src: float('inf')})
        
        while True:
            max_flow = 0
            max_loc = None
            
            # find the unvisited node with the highest capacity to it
            for i in graph:
                if flow[i] > max_flow and i not in visited:
                    max_flow = flow[i]
                    max_loc = i
            
            if max_loc is None or max_loc == sink:
                break

            visited.add(max_loc)

            # update its neighbors
            for nei, capacity in graph[max_loc].items():
                if flow[nei] < min(max_flow, capacity):
                    prev[nei] = max_loc
                    flow[nei] = min(max_flow, capacity)

        # no path
        if max_loc is None:
            break

        # add that flow to the network and update capacity appropriately
        path_capacity = flow[sink]
        total_flow += path_capacity 
        curr = sink

        # for each arc (prev(curr) -> curr) on path:
        while curr != src:
            parent = prev[curr]
            graph[parent][curr] -= path_capacity
            graph[curr][parent] += path_capacity
            curr = parent

ford_fulkerson(f'{c1 - 1}B', f'{c2 - 1}A')

def DFS(start, seen):
    seen.add(start)
    for nei, cap in graph[start].items():
        if cap > 0 and nei not in seen:
            DFS(nei, seen)

seen = set()
DFS(f'{c1 - 1}B', seen)

ans = []
for i in range(N):
    if f'{i}A' in seen and f'{i}B' not in seen:
        ans.append(i + 1)

print(len(ans))
print(*ans)