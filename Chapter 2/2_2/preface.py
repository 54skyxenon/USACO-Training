"""
ID: bwliang1
LANG: PYTHON3
TASK: preface
"""

import sys
from collections import Counter
from functools import lru_cache

PROBLEM_NAME = 'preface'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

@lru_cache(None)
def dp(i):
    if i < len(ones):
        return Counter(ones[i])

    if i >= 1000:
        return Counter({'M': 1}) + dp(i - 1000)
    
    if i >= 900:
        return Counter({'M': 1, 'C': 1}) + dp(i - 900)
    
    if i >= 500:
        return Counter({'D': 1}) + dp(i - 500)
    
    if i >= 400:
        return Counter({'D': 1, 'C': 1}) + dp(i - 400)
    
    if i >= 100:
        return Counter({'C': 1}) + dp(i - 100)
    
    if i >= 90:
        return Counter({'C': 1, 'X': 1}) + dp(i - 90)
    
    if i >= 50:
        return Counter({'L': 1}) + dp(i - 50)
    
    if i >= 40:
        return Counter({'L': 1, 'X': 1}) + dp(i - 40)
    
    # i >= 10
    return Counter({'X': 1}) + dp(i - 10)

n = int(input())
ans = sum([dp(i) for i in range(1, n + 1)], Counter())

for letter in sorted(ans.keys(), key=lambda k: mapping[k]):
    print(letter, ans[letter])