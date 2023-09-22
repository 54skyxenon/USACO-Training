'''
ID: bwliang1
LANG: PYTHON3
TASK: clocks
'''

import sys
from itertools import product

PROBLEM_NAME = 'clocks'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

moves = ['ABDE', 'ABC', 'BCEF', 'ADG', 'BDEFH', 'CFI', 'DEGH', 'GHI', 'EFHI']
equations = [[] for _ in range(9)]

for i, move in enumerate(moves):
    for letter in move:
        equations[ord(letter) - ord('A')].append(i)

inputs = input() + ' ' + input() + ' ' + input()
inputs = list(map(int, inputs.split()))

for i in range(9):
    rhs = -(inputs[i] // 3)
    equations[i].append(rhs % 4)

def lexicographic(assignment):
    return ' '.join(map(str, sum([[i + 1] * multiple for i, multiple in enumerate(assignment)], [])))

def satisfies(assignment, equation):
    return sum(assignment[move] for move in equation[:-1]) % 4 == equation[-1]

best = (float('inf'), None)
for assignment in product(*[range(4) for _ in range(9)]):
    if all(satisfies(assignment, equation) for equation in equations):
        best = min(best, (sum(assignment), lexicographic(assignment)))

print(best[1])