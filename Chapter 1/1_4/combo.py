'''
ID: bwliang1
LANG: PYTHON3
TASK: combo
'''

import sys

PROBLEM_NAME = 'combo'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
fj_combo = list(map(int, input().split()))
master_combo = list(map(int, input().split()))

dials = list(range(1, n + 1))

def close(i, x, combo):
    can_match = {dials[x - 1], dials[x % n], dials[(x + 1) % n]}

    if x - 2 >= -len(dials):
        can_match.add(dials[x - 2])

    if x - 3 >= -len(dials):
        can_match.add(dials[x - 3])

    return combo[i] in can_match

ans = set()
for a in range(1, n + 1):
    if close(0, a, fj_combo):
        for b in range(1, n + 1):
            if close(1, b, fj_combo):
                for c in range(1, n + 1):
                    if close(2, c, fj_combo):
                        ans.add((a, b, c))

    if close(0, a, master_combo):
        for b in range(1, n + 1):
            if close(1, b, master_combo):
                for c in range(1, n + 1):
                    if close(2, c, master_combo):
                        ans.add((a, b, c))

print(len(ans))