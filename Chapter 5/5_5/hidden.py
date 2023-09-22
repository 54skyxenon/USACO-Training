'''
ID: bwliang1
LANG: PYTHON3
TASK: hidden
'''

import sys

PROBLEM_NAME = 'hidden'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

l = int(input())
S = ''.join(l.strip() for l in sys.stdin.readlines())

def my_cmp(a, b):
    a_ptr = a
    b_ptr = b
    
    while True:
        letter_a = S[a_ptr]
        letter_b = S[b_ptr]

        if letter_a != letter_b:
            return a if ord(letter_a) < ord(letter_b) else b
        
        a_ptr = (a_ptr + 1) % l
        b_ptr = (b_ptr + 1) % l

        if a_ptr >= b:
            return a
        
def divide_and_conquer(l, r):
    if l >= r:
        return l
    
    mid = (l + r) // 2
    best_l = divide_and_conquer(l, mid)
    best_r = divide_and_conquer(mid + 1, r)
    return my_cmp(best_l, best_r)

print(divide_and_conquer(0, len(S) - 1))