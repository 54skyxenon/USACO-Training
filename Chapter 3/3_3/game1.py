'''
ID: bwliang1
LANG: PYTHON3
TASK: game1
'''

import sys
from functools import cache

PROBLEM_NAME = 'game1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
board = list(map(int, ' '.join(sys.stdin.readlines()).split()))

@cache
def dp(i, j):
    if i == j:
        return (board[i], 0)
    
    other_left, this_left = dp(i + 1, j)
    other_right, this_right = dp(i, j - 1)
    return max((this_left + board[i], other_left), (this_right + board[j], other_right))

print(*dp(0, len(board) - 1))