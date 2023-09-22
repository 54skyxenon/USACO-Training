'''
ID: bwliang1
LANG: PYTHON3
TASK: prefix
'''

import sys

PROBLEM_NAME = 'prefix'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

# This was a PITA
all_input = ''.join(sys.stdin.readlines())

P, S = all_input.split('.')
P = P.split()
S = ''.join(S.split())

n = len(S)
dp = [False] * (n + 1)
dp[0] = True
ans = 0

for i in range(1, n + 1):
    for p in P:
        if S[i - len(p):i] == p:
            dp[i] = dp[i] or dp[i - len(p)]
    
    if dp[i]:
        ans = i

print(ans)