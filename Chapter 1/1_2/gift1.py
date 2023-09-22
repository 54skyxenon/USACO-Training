"""
ID: bwliang1
LANG: PYTHON3
TASK: gift1
"""

import sys

PROBLEM_NAME = 'gift1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

np = int(input())

people = []
gifts = dict()
for _ in range(np):
    name = input()
    gifts[name] = 0
    people.append(name)

for _ in range(np):
    giver = input()
    money, num_beneficiaries = map(int, input().split())

    give, keep = divmod(money, num_beneficiaries) if num_beneficiaries > 0 else (0, money)
    gifts[giver] = gifts[giver] - money + keep

    for _ in range(num_beneficiaries):
        gifts[input()] += give

for name in people:
    print(name, gifts[name])