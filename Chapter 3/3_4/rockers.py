'''
ID: bwliang1
LANG: PYTHON3
TASK: rockers
'''

import sys
from functools import cache

PROBLEM_NAME = 'rockers'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n, t, m = map(int, input().split())
songs = list(map(int, input().split()))

@cache
def dp(i, time_left, disks_left):
    if i == n or disks_left == 0:
        return 0
    
    if songs[i] > time_left:
        # OPTIONS:
        # 1. stay here using a new disk
        # 2. move to next song on current disk
        return max(dp(i, t, disks_left - 1), dp(i + 1, time_left, disks_left))
    else:
        # OPTIONS:
        # 1. put current song on disk and move to next song
        # 2. skip current song and move to next song
        return max(1 + dp(i + 1, time_left - songs[i], disks_left), dp(i + 1, time_left, disks_left))
    
print(dp(0, t, m))