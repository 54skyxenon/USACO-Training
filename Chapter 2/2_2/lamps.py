'''
ID: bwliang1
LANG: PYTHON3
TASK: lamps
'''

import sys
from itertools import product

PROBLEM_NAME = 'lamps'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
c = int(input())
on = list(map(int, input().split()))[:-1]
off = list(map(int, input().split()))[:-1]

def works(setting):
    p1, p2, p3, p4 = map(int, setting)

    for j in off:
        if j % 2 == 1 and (j - 1) % 3 == 0:
            if (p1 + p2 + p4) % 2 != 1:
                return False
        elif j % 2 == 0 and (j - 1) % 3 == 0:
            if (p1 + p3 + p4) % 2 != 1:
                return False
        elif j % 2 == 1 and (j - 1) % 3 != 0:
            if (p1 + p2) % 2 != 1:
                return False
        else: # j % 2 == 0 and (j - 1) % 3 != 0:
            if (p1 + p3) % 2 != 1:
                return False

    for j in on:
        if j % 2 == 1 and (j - 1) % 3 == 0:
            if (p1 + p2 + p4) % 2 != 0:
                return False
        elif j % 2 == 0 and (j - 1) % 3 == 0:
            if (p1 + p3 + p4) % 2 != 0:
                return False
        elif j % 2 == 1 and (j - 1) % 3 != 0:
            if (p1 + p2) % 2 != 0:
                return False
        else: # j % 2 == 0 and (j - 1) % 3 != 0:
            if (p1 + p3) % 2 != 0:
                return False

    return (p1 + p2 + p3 + p4) % 2 == c % 2

def add_to_answer(path, ans):
    answer = ['1'] * n

    for i in range(1, n + 1):
        if i % 2 == 1 and (i - 1) % 3 == 0:
            answer[i - 1] = str(1 - (path[0] + path[1] + path[3]) % 2)
        elif i % 2 == 0 and (i - 1) % 3 == 0:
            answer[i - 1] = str(1 - (path[0] + path[2] + path[3]) % 2)
        elif i % 2 == 1 and (i - 1) % 3 != 0:
            answer[i - 1] = str(1 - (path[0] + path[1]) % 2)
        else: #if i % 2 == 0 and (i - 1) % 3 != 0:
            answer[i - 1] = str(1 - (path[0] + path[2]) % 2)

    ans.add(''.join(answer))

def partitions(setting, remaining):
    needed_parity_1 = int(setting[0])
    needed_parity_2 = int(setting[1])

    ans = []

    for i in range(needed_parity_1, min(3, remaining + 1), 2):
        for j in range(needed_parity_2, min(3, remaining - i + 1), 2):
            ans.append([i, j])

    return ans

settings = ['{0:b}'.format(i).zfill(4) for i in range(2 ** 4)]

# the parities we try to make for each type of button press
allowed = dict()
ans = set()
for setting in settings:
    if works(setting):
        for i in range(min(3, c + 1)):
            for parts1, parts2 in product(partitions(setting[:2], i), partitions(setting[2:], c - i)):
                add_to_answer(parts1 + parts2, ans)

if not ans:
    print('IMPOSSIBLE')
else:
    for a in sorted(ans):
        print(a)