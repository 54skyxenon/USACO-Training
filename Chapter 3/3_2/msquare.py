'''
ID: bwliang1
LANG: PYTHON3
TASK: msquare
'''

import sys
from collections import deque

PROBLEM_NAME = 'msquare'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

target = input().replace(' ', '')
start = '12345678'
Q = deque([start])
seen = {start: ('', '')}

def A(sequence):
    return sequence[::-1]

def B(sequence):
    matrix = [list(sequence[:4]), list(sequence[4:][::-1])]
    matrix[0] = matrix[0][3:] + matrix[0][:3]
    matrix[1] = matrix[1][3:] + matrix[1][:3]
    return ''.join(matrix[0] + matrix[1][::-1])

def C(sequence):
    matrix = [list(sequence[:4]), list(sequence[4:][::-1])]
    matrix[0][1], matrix[0][2], matrix[1][2], matrix[1][1] = matrix[1][1], matrix[0][1], matrix[0][2], matrix[1][2]
    return ''.join(matrix[0] + matrix[1][::-1])

ans = []
action = ['A', 'B', 'C']

while Q:
    curr = Q.popleft()

    if curr == target:
        ptr = curr
        while ptr != '':
            ans.append(seen[ptr][1])
            ptr = seen[ptr][0]
        break

    for i, nei in enumerate([A(curr), B(curr), C(curr)]):
        if nei not in seen:
            seen[nei] = (curr, action[i])
            Q.append(nei)

ans = ''.join(reversed(ans))
print(len(ans))
for i in range(0, max(1, len(ans)), 60):
    print(ans[i:i+60])