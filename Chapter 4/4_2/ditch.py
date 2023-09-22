'''
ID: bwliang1
LANG: PYTHON3
TASK: ditch
'''

import sys
from collections import defaultdict

PROBLEM_NAME = 'ditch'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, m = map(int, input().split())

graph = [defaultdict(int) for _ in range(m)]
for _ in range(n):
    s, e, c = map(int, input().split())
    graph[s - 1][e - 1] += c

def ford_fulkerson(src, sink):
    total_flow = 0
    
    while True:
        # find path with highest capacity from src to sink, using modified Dijkstra's
        prev = dict()
        visited = [False] * m
        flow = [0] * m
        flow[src] = float('inf')
        
        while True:
            max_flow = 0
            max_loc = None
            
            # find the unvisited node with the highest capacity to it
            for i in range(m):
                if flow[i] > max_flow and not visited[i]:
                    max_flow = flow[i]
                    max_loc = i
            
            if max_loc is None or max_loc == sink:
                break

            visited[max_loc] = True

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
            next = prev[curr]
            graph[next][curr] -= path_capacity
            graph[curr][next] += path_capacity
            curr = next

    return total_flow

print(ford_fulkerson(0, m - 1))