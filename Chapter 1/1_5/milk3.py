"""
ID: bwliang1
LANG: PYTHON3
TASK: milk3
"""

import sys

PROBLEM_NAME = 'milk3'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

a, b, c = map(int, input().split())
capacities = [a, b, c]
states = set()
ans = set()

def DFS(state):
    if state[0] == 0:
        ans.add(state[2])

    for i in range(3):
        for j in range(3):
            if i != j:
                take = min(state[i], capacities[j] - state[j])
                new_state = state[:]
                new_state[i] -= take
                new_state[j] += take

                if tuple(new_state) not in states:
                    states.add(tuple(new_state))
                    DFS(new_state)

states.add((0, 0, c))
DFS([0, 0, c])
print(' '.join(map(str, sorted(ans))))