'''
ID: bwliang1
LANG: PYTHON3
TASK: milk2
'''

import sys

PROBLEM_NAME = 'milk2'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

def merge(intervals):
    new_intervals = []
    
    for start, end in sorted(intervals):
        if not new_intervals or new_intervals[-1][1] < start:
            new_intervals.append([start, end])
        else:
            new_intervals[-1][1] = max(new_intervals[-1][1], end)
    
    return new_intervals

intervals = []
for _ in range(n):
    intervals.append(tuple(map(int, input().split())))
intervals = merge(intervals)

max_continuous = max(e - s for s, e in intervals)
max_gap = max([intervals[i + 1][0] - intervals[i][1] for i in range(len(intervals) - 1)] or [0])
print(max_continuous, max_gap)