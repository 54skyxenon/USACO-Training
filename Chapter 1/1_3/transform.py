'''
ID: bwliang1
LANG: PYTHON3
TASK: transform
'''

import sys

PROBLEM_NAME = 'transform'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

def cw(mat):
    return list(map(list, zip(*mat[::-1])))

def ccw(mat):
    return cw(cw(cw(mat)))

def reflect(mat):
    return [row[::-1] for row in mat]

before = []
for _ in range(n):
    before.append(list(input()))

after = []
for _ in range(n):
    after.append(list(input()))

def solve():
    if cw(before) == after:
        return 1
    
    if cw(cw(before)) == after:
        return 2
    
    if ccw(before) == after:
        return 3

    if reflect(before) == after:
        return 4
    
    if cw(reflect(before)) == after or cw(cw(reflect(before))) == after or ccw(reflect(before)) == after:
        return 5

    if before == after:
        return 6
    
    return 7

print(solve())