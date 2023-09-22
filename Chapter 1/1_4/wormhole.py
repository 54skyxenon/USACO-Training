'''
ID: bwliang1
LANG: PYTHON3
TASK: wormhole
'''

import sys

PROBLEM_NAME = 'wormhole'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

wormholes = []
for _ in range(n):
    wormholes.append(tuple(map(int, input().split())))

next_on_right = [-1] * n
for i, (x1, y1) in enumerate(wormholes):
    for j, (x2, y2) in enumerate(wormholes):
        if x2 > x1 and y1 == y2:
            if next_on_right[i] == -1 or x2 < wormholes[next_on_right[i]][0]:
                next_on_right[i] = j

def has_cycle(pairs):
    partner = dict()
    for p1, p2 in pairs:
        partner[p1] = p2
        partner[p2] = p1
    
    for start in range(n):
        pos = start
        seen = set([start])
        for _ in range(n):
            if next_on_right[partner[pos]] == -1:
                break

            pos = next_on_right[partner[pos]]
            if pos in seen:
                return 1
            seen.add(pos)
        
    return 0

def DFS(remaining, pairs):
    if not remaining:
        return has_cycle(pairs)

    ans = 0
    for j in range(1, len(remaining)):
        pairs.append((remaining[0], remaining[j]))
        ans += DFS(remaining[1:j] + remaining[j + 1:], pairs)
        pairs.pop()

    return ans

print(DFS(list(range(n)), []))