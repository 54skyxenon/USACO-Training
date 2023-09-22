'''
ID: bwliang1
LANG: PYTHON3
TASK: race3
'''

import sys
from collections import deque
from copy import deepcopy

PROBLEM_NAME = 'race3'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

graph = []
while (line := input()) != '-1':
    graph.append([])
    graph[-1].extend(list(map(int, line.split()[:-1])))

def cut_out(graph, s):
    new_graph = deepcopy(graph)
    new_graph[s].clear()

    for adj in new_graph:
        if s in adj:
            adj.remove(s)

    return new_graph

def reachable(graph, src, target):
    Q = deque([src])
    seen = set([src])

    while Q:
        curr = Q.popleft()
        if curr == target:
            return True
        
        for nei in graph[curr]:
            if nei not in seen:
                seen.add(nei)
                Q.append(nei)

    return False

def reverse_graph(graph):
    graph_reversed = [[] for _ in graph]

    for i, adj in enumerate(graph):
        for j in adj:
            graph_reversed[j].append(i)

    return graph_reversed

unavoidable = []
for i in range(1, len(graph) - 1):
    if not reachable(cut_out(graph, i), 0, len(graph) - 1):
        unavoidable.append(i)
print(len(unavoidable), *unavoidable)

def is_splitting_point(s):
    graph_1, graph_2 = deepcopy(graph), deepcopy(graph)
    
    # Verify 0 to S is well-formed
    graph_1[s].clear()
    graph_1_inv = reverse_graph(graph_1)

    course_1 = set([0])
    Q1 = deque([0])
    while Q1:
        curr = Q1.popleft()
        for nei in graph_1[curr]:
            if nei not in course_1:
                course_1.add(nei)
                Q1.append(nei)

    course_1_inv = set([s])
    Q1_inv = deque([s])
    while Q1_inv:
        curr = Q1_inv.popleft()
        for nei in graph_1_inv[curr]:
            if nei not in course_1_inv:
                course_1_inv.add(nei)
                Q1_inv.append(nei)

    if not course_1.issubset(course_1_inv):
        return False

    # Verify S to N is well-formed
    for adj in graph_2:
        if s in adj:
            adj.remove(s)
    graph_2_inv = reverse_graph(graph_2)

    course_2 = set([s])
    Q2 = deque([s])
    while Q2:
        curr = Q2.popleft()
        for nei in graph_2[curr]:
            if nei not in course_2:
                course_2.add(nei)
                Q2.append(nei)

    course_2_inv = set([len(graph) - 1])
    Q2_inv = deque([len(graph) - 1])
    while Q2_inv:
        curr = Q2_inv.popleft()
        for nei in graph_2_inv[curr]:
            if nei not in course_2_inv:
                course_2_inv.add(nei)
                Q2_inv.append(nei)
    
    if not course_2.issubset(course_2_inv):
        return False

    union = course_1 | course_2
    intersection = course_1 & course_2
    return len(union) == len(graph) and intersection == {s}
    
splitting_points = [s for s in unavoidable if is_splitting_point(s)]
print(len(splitting_points), *splitting_points)