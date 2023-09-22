'''
ID: bwliang1
LANG: PYTHON3
TASK: kimbits
'''

import sys
from math import comb

PROBLEM_NAME = 'kimbits'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, l, i = map(int, input().split())

def solve(position, remaining_bits, to_traverse):
    if position == n + 1:
        return ''

    skipped = sum(comb(n - position, bits) for bits in range(remaining_bits + 1))
    if skipped < to_traverse and remaining_bits > 0:
        return '1' + solve(position + 1, remaining_bits - 1, to_traverse - skipped)
    else:
        return '0' + solve(position + 1, remaining_bits, to_traverse)

print(solve(1, l, i))