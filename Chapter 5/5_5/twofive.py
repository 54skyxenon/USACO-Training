'''
ID: bwliang1
LANG: PYTHON3
TASK: twofive
'''

# Adapted from: https://blog.csdn.net/qq_36911709/article/details/84206564
 
import sys
from string import ascii_uppercase
from functools import cache

PROBLEM_NAME = 'twofive'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

buffer = [''] * 25

@cache
def dp(a, b, c, d, e, s):
    ''' DP state is the number of remaining configurations with (a, b, c, d, e) spots filled on each of the five rows, with the current char to place being s. 
        In a Young tableau, a <= b <= c <= d <= e must hold at any given time.
    '''
    if s == 'Z':
        return 1

    ans = 0
    next_chr = chr(ord(s) + 1)

    if a < 5 and (buffer[a] == '' or buffer[a] == s):
        ans += dp(a + 1, b, c, d, e, next_chr)

    if b < a and (buffer[b + 5] == '' or buffer[b + 5] == s):
        ans += dp(a, b + 1, c, d, e, next_chr)

    if c < b and (buffer[c + 10] == '' or buffer[c + 10] == s):
        ans += dp(a, b, c + 1, d, e, next_chr)

    if d < c and (buffer[d + 15] == '' or buffer[d + 15] == s):
        ans += dp(a, b, c, d + 1, e, next_chr)

    if e < d and (buffer[e + 20] == '' or buffer[e + 20] == s):
        ans += dp(a, b, c, d, e + 1, next_chr)

    return ans

def sequence_to_index(seq):
    idx = 0

    for i, letter in enumerate(seq):
        for c in ascii_uppercase:
            buffer[i] = c
            if c == letter:
                break

            dp.cache_clear()
            idx += dp(0, 0, 0, 0, 0, 'A')
    
    return idx + 1

def index_to_sequence(idx):
    for i in range(len(buffer)):
        for c in ascii_uppercase:
            buffer[i] = c

            dp.cache_clear()
            skipped = dp(0, 0, 0, 0, 0, 'A')
            if skipped >= idx:
                break
            else:
                idx -= skipped

    return ''.join(buffer)

if input() == 'W':
    print(sequence_to_index(input()))
else:
    print(index_to_sequence(int(input())))