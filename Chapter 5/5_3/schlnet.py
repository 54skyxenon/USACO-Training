'''
ID: bwliang1
LANG: PYTHON3
TASK: schlnet
'''

import sys
from collections import defaultdict

PROBLEM_NAME = 'schlnet'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

class Graph:
    ''' SCC implementation adapted from Neelam Yadav: https://www.geeksforgeeks.org/strongly-connected-components '''
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, scc):
        # Mark the current node as visited and print it
        visited[v] = True
        scc.add(v)
        
        # Recurse for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, scc)

    def fill_order(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        
        # Recurse for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        
        stack = stack.append(v)

    def transpose(self):
        g = Graph(self.V)

        # Recurse for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        
        return g

    def get_sccs(self):
        stack = []
        
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.V
        
        # Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        # Create a reversed graph
        g_inv = self.transpose()
            
        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * self.V

        sccs = []

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = set()
                g_inv.dfs(i, visited, scc)
                sccs.append(scc)
        
        return sccs

n = int(input())

g = Graph(n)
edges = []
for i in range(n):
    for nei in map(int, input().split()):
        if nei != 0:
            g.add_edge(i, nei - 1)
            edges.append((i, nei - 1))

scc_data = g.get_sccs()
scc_of = dict()
for scc_id, scc in enumerate(scc_data):
    for v in scc:
        scc_of[v] = scc_id

inedges = defaultdict(set)
scc_graph = [set() for _ in scc_data]
for src, dest in edges:
    src_scc = scc_of[src]
    dest_scc = scc_of[dest]
    if src_scc != dest_scc:
        scc_graph[src_scc].add(dest_scc)
        inedges[dest_scc].add(src_scc)

roots = set()
for scc_id in range(len(scc_data)):
    if len(inedges[scc_id]) == 0:
        roots.add(scc_id)

leaves = set(i for i in range(len(scc_graph)) if not scc_graph[i])

# For subtask A
print(len(roots))

# For subtask B
if len(scc_data) == 1:
    print('0')
else:
    print(max(len(roots), len(leaves)))