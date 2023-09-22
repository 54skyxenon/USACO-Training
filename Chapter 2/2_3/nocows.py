'''
ID: bwliang1
LANG: PYTHON3
TASK: nocows
'''

import sys
from functools import cache

PROBLEM_NAME = 'nocows'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

MOD = 9901

@cache
def dp_k_prefix(n, k):
    # Prefix sum to speed up summing product of DP states
    if k == 1:
        return dp(n, k)
    
    return dp(n, k) + dp_k_prefix(n, k - 1)

@cache
def dp(n, k):
    # Can't make a tree with even # of nodes
    # OR not even a perfect tree makes n nodes
    if n % 2 == 0 or 2 ** k - 1 < n:
        return 0

    # Only a perfect tree fits the criterion of (n, k)
    if 2 ** k - 1 == n:
        return 1
    
    ans = 0
    remaining = n - 1
    states = set()

    # Left and right are both odd and add to the number remaining
    # True/False are used to fix height (k - 1) to either left and right node count requirement
    for left in range(1, remaining, 2):
        right = remaining - left
        states.add((left, right, True, False))
        states.add((left, right, False, True))
        states.add((left, right, True, True))

    # Be careful not to overcount with unique states
    for l, r, fixed_l, fixed_r in states:
        if fixed_l and fixed_r:
            ans += dp(l, k - 1) * dp(r, k - 1)
        elif fixed_l and not fixed_r:
            ans += dp(l, k - 1) * dp_k_prefix(r, k - 2)
        else:
            ans += dp_k_prefix(l, k - 2) * dp(r, k - 1)
        ans %= MOD

    return ans

N, K = map(int, input().split())
print(dp(N, K))