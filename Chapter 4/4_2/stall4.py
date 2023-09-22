'''
ID: bwliang1
LANG: PYTHON3
TASK: stall4
'''

import sys
from collections import Counter

PROBLEM_NAME = 'stall4'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, m = map(int, input().split())

stalls = [set() for _ in range(m)]
for i in range(n):
    preferences = [int(x) - 1 for x in input().split()[1:]]
    for preference in preferences:
        stalls[preference].add(i)

stalls = [stall for stall in stalls if len(stall) > 0]
rarity = sum([Counter(stall) for stall in stalls], Counter())

ans = 0
while stalls:
    best_stall = 0
    rarest_cow = min(stalls[0], key=lambda c: rarity[c])
    best_rarity = rarity[rarest_cow]

    for i in range(1, len(stalls)):
        rarest_cow_here = min(stalls[i], key=lambda c: rarity[c])
        best_rarity_here = rarity[rarest_cow_here]

        if (len(stalls[i]), best_rarity_here) < (len(stalls[best_stall]), best_rarity):
            best_stall = i
            rarest_cow = rarest_cow_here
            best_rarity = best_rarity_here

    new_stalls = []
    for i, stall in enumerate(stalls):
        if rarest_cow in stall:
            stall.remove(rarest_cow)
            rarity[rarest_cow] -= 1
        
        if i != best_stall and len(stall) > 0:
            new_stalls.append(stall)
        else:
            rarity -= Counter(stall)
    
    stalls = new_stalls
    ans += 1

print(ans)