"""
ID: bwliang1
LANG: PYTHON3
TASK: pprime
"""

import sys

PROBLEM_NAME = 'pprime'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

a, b = map(int, input().split())

def is_prime(palindrome):
    if not palindrome or palindrome.startswith('0'):
        return False
    
    num = int(palindrome)

    if not a <= num <= b:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

ans = set()

def DFS(palindrome):
    if len(palindrome) > len(str(b)) or (palindrome and int(palindrome) > b):
        return
    
    if is_prime(palindrome):
        ans.add(palindrome)

    for digit in range(10):
        new_pal = str(digit) + palindrome + str(digit)
        DFS(new_pal)

DFS('')
for digit in range(10):
    DFS(str(digit))

for a in sorted(map(int, ans)):
    print(a)