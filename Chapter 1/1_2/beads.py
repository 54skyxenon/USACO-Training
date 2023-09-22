"""
ID: bwliang1
LANG: PYTHON3
TASK: beads
"""

import sys

PROBLEM_NAME = 'beads'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
beads = input()
ans = 0

for shift in range(n):
    new_beads = beads[shift:] + beads[:shift]
    new_beads_other = new_beads[::-1]

    seen_here = set()
    seen_here_count = 0
    for i in range(n):
        if (seen_here | set(new_beads[i])).issuperset({'r', 'b'}):
            break
        else:
            seen_here.add(new_beads[i])
            seen_here_count += 1

    seen_other = set()
    seen_other_count = 0
    for i in range(n):
        if (seen_other | set(new_beads_other[i])).issuperset({'r', 'b'}):
            break
        else:
            seen_other.add(new_beads_other[i])
            seen_other_count += 1

    ans = max(ans, min(n, seen_here_count + seen_other_count))

print(ans)