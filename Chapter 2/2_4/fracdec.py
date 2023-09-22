'''
ID: bwliang1
LANG: PYTHON3
TASK: fracdec
'''

import sys

PROBLEM_NAME = 'fracdec'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

LINE_LENGTH = 76
n, d = map(int, input().split())

integral, minuend = divmod(n, d)
seen = dict()
mantissa = []
cycle_start = None
i = 0

while True:
    digit, next_minuend = divmod(minuend * 10, d)

    state = (digit, next_minuend)
    if state in seen:
        cycle_start = seen[state]
        break

    seen[state] = i
    mantissa.append(digit)
    minuend = next_minuend
    i += 1

nonrepeating = ''.join(map(str, mantissa[:cycle_start]))
repeating = f"({''.join(map(str, mantissa[cycle_start:]))})"
if repeating.count('0') == len(repeating) - 2:
    repeating = ''

fractional = nonrepeating + repeating
if not fractional:
    fractional = '0'

expansion = f'{integral}.{fractional}'
for i in range(0, len(expansion), LINE_LENGTH):
    print(expansion[i:i+LINE_LENGTH])