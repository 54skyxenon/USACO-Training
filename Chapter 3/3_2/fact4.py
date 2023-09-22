'''
ID: bwliang1
LANG: PYTHON3
TASK: fact4
'''

import sys
from math import ceil
from collections import Counter
from functools import reduce

PROBLEM_NAME = 'fact4'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())

def is_prime(x):
    return all(x % i != 0 for i in range(2, ceil(x ** 0.5 + 1)))

primes = [2] + [i for i in range(3, n + 1) if is_prime(i)]
prime_counts = Counter()
for i in range(1, n + 1):
    for p in primes:
        while i % p == 0:
            prime_counts[p] += 1
            i //= p

ten_factors = min(prime_counts[5], prime_counts[2])
prime_counts[2] -= ten_factors
prime_counts[5] -= ten_factors

all_factors = sum([[p] * cnt for p, cnt in prime_counts.items()], [])
print(reduce(lambda a, b: a * b % 10, all_factors, 1))