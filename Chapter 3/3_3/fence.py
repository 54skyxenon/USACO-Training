'''
ID: bwliang1
LANG: PYTHON3
TASK: fence
'''

import sys
sys.setrecursionlimit(200000)

MAX_FENCES = 500

PROBLEM_NAME = 'fence'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

f = int(input())
graph = [[] for _ in range(MAX_FENCES)]
for _ in range(f):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

path_start = None
for i in range(MAX_FENCES):
    degree = len(graph[i])
    if degree % 2 == 1:
        path_start = i
        break

ans = []
def DFS(root):
    while graph[root]:
        nei = min(graph[root])
        graph[root].remove(nei)
        graph[nei].remove(root)
        DFS(nei)
    
    ans.append(root)

# No Eulerian circuit exists, start path at lower node
if path_start is not None:
    DFS(path_start)
# Follow the Eulerian circuit starting at 1
else:
    DFS(min(i for i in range(MAX_FENCES) if graph[i]))

print(*[node + 1 for node in reversed(ans)], sep='\n')