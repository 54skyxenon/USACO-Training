"""
ID: bwliang1
LANG: PYTHON3
TASK: sort3
"""

import sys

PROBLEM_NAME = 'sort3'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))

ans = 0
ones = A.count(1)
twos = A.count(2)
threes = A.count(3)

# Swap the OBVIOUS ones first
# i.e. there's two incorrect indices where swapping them would land them in both correct regions
while True:
    three_in_one_idx = None
    two_in_one_idx = None
    three_in_two_idx = None
    one_in_two_idx = None
    two_in_three_idx = None
    one_in_three_idx = None

    for i in range(ones):
        if A[i] == 2:
            two_in_one_idx = i
        elif A[i] == 3:
            three_in_one_idx = i

    for i in range(ones, ones + twos):
        if A[i] == 1:
            one_in_two_idx = i
        elif A[i] == 3:
            three_in_two_idx = i

    for i in range(ones + twos, n):
        if A[i] == 1:
            one_in_three_idx = i
        elif A[i] == 2:
            two_in_three_idx = i

    if three_in_one_idx is not None and one_in_three_idx is not None:
        A[three_in_one_idx], A[one_in_three_idx] = A[one_in_three_idx], A[three_in_one_idx]
        ans += 1
        continue

    if two_in_one_idx is not None and one_in_two_idx is not None:
        A[two_in_one_idx], A[one_in_two_idx] = A[one_in_two_idx], A[two_in_one_idx]
        ans += 1
        continue

    if two_in_three_idx is not None and three_in_two_idx is not None:
        A[two_in_three_idx], A[three_in_two_idx] = A[three_in_two_idx], A[two_in_three_idx]
        ans += 1
        continue

    break

# If still not sorted, we have no choice but to sort from beginning
for i in range(n):
    if i < ones:
        if A[i] != 1:
            ans += 1
            for j in range(n - 1, i, -1):
                if A[j] == 1:
                    A[i], A[j] = A[j], A[i]
                    break
    elif i < ones + twos:
        if A[i] != 2:
            ans += 1
            for j in range(n - 1, i, -1):
                if A[j] == 2:
                    A[i], A[j] = A[j], A[i]
                    break
    else:
        break

print(ans)