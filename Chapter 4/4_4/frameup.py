'''
ID: bwliang1
LANG: PYTHON3
TASK: frameup
'''

import sys
from collections import defaultdict

PROBLEM_NAME = 'frameup'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

h, w = map(int, input().split())

frames = []
for _ in range(h):
    frames.append(input())

letters = sorted(set(c for c in ''.join(frames) if c.isupper()))

def build():
    letter_bounds = defaultdict(lambda: [float('inf'), float('inf'), float('-inf'), float('-inf')])
    can_go_after = dict((l, set(letters)) for l in letters)

    for r in range(h):
        for c in range(w):
            letter = frames[r][c]
            if letter.isupper():
                letter_bounds[letter][0] = min(r, letter_bounds[letter][0])
                letter_bounds[letter][1] = min(c, letter_bounds[letter][1])
                letter_bounds[letter][2] = max(r, letter_bounds[letter][2])
                letter_bounds[letter][3] = max(c, letter_bounds[letter][3])

    for letter in letters:
        r1, c1, r2, c2 = letter_bounds[letter]
        for c in range(c1, 1 + c2):
            if frames[r1][c] != letter:
                can_go_after[frames[r1][c]].discard(letter)

            if frames[r2][c] != letter:
                can_go_after[frames[r2][c]].discard(letter)

        for r in range(r1, 1 + r2):
            if frames[r][c1] != letter:
                can_go_after[frames[r][c1]].discard(letter)

            if frames[r][c2] != letter:
                can_go_after[frames[r][c2]].discard(letter)

    return can_go_after

graph = build()

def DFS(path, remaining):
    # Prune the search if we can't make it anyways
    if len(path) + len(remaining) < len(letters):
        return

    if not remaining:
        print(''.join(path))
        return
    
    for nxt in sorted(graph[path[-1]]):
        if nxt in remaining:
            remaining.discard(nxt)
            removed = set()
            for letter in letters:
                if letter not in graph[path[-1]] and letter in remaining:
                    remaining.remove(letter)
                    removed.add(letter)
            
            path.append(nxt)
            DFS(path, remaining)
            path.pop()

            remaining.update(removed)
            remaining.add(nxt)

for i, l in enumerate(letters):
    DFS([l], set(letters) - {l})