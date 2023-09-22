'''
ID: bwliang1
LANG: PYTHON3
TASK: wissqu
'''

import sys
from itertools import product

PROBLEM_NAME = 'wissqu'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

fields = []
for _ in range(4):
    fields.append(list(input()))

calves = [['A', 3], ['B', 3], ['C', 3], ['D', 4], ['E', 3]]
best_ans = []

def path_state(path):
    ''' Flatten path into a 16-char string, with unused cells marked with Xs '''
    state = [['X'] * 4 for _ in range(4)]

    for herd_type, r, c in path:
        state[r][c] = herd_type

    return ''.join(''.join(row) for row in state)

memo = dict()

def dp(path):
    state = path_state(path)
    if state in memo:
        return memo[state]

    if len(path) == 16:
        if not best_ans:
            best_ans.extend(path)
        return 1
    
    ans = 0
    occupied = set((r, c) for _, r, c in path)

    for j, (herd_type, herd_count) in enumerate(calves):
        if herd_count == 0:
            continue

        if len(path) == 0 and herd_type != 'D':
            continue

        for r, c in product(range(4), range(4)):
            if (r, c) in occupied:
                continue

            if fields[r][c] == herd_type:
                continue

            neighbors_good = True
            for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4 and fields[nr][nc] == herd_type:
                    neighbors_good = False
                    break

            if not neighbors_good:
                continue

            path.append((herd_type, r, c))
            calves[j][1] -= 1
            old_herd_type, fields[r][c] = fields[r][c], herd_type

            ans += dp(path)
            
            fields[r][c] = old_herd_type
            calves[j][1] += 1
            path.pop()

    memo[state] = ans
    return ans

ans = dp([])

for herd_type, r, c in best_ans:
    print(herd_type, r + 1, c + 1)

print(ans)