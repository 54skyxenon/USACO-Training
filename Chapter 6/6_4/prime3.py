'''
ID: bwliang1
LANG: PYTHON3
TASK: prime3
'''

import sys
from collections import defaultdict

PROBLEM_NAME = 'prime3'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

PRIME_LIMIT = 100000

choice = defaultdict(list)
matrix = [[10] * 5 for _ in range(5)]
is_prime = [True] * PRIME_LIMIT
ans = []

def read_prime(locations):
    return sum(10 ** i * matrix[r][c] for i, (r, c) in enumerate(locations[::-1]))

def add_answer():
    diagonal_1 = read_prime([(j, j) for j in range(5)])
    if not is_prime[diagonal_1] or digit_sum(diagonal_1) != target_sum:
        return
    
    diagonal_2 = read_prime([(4 - j, j) for j in range(5)])
    if not is_prime[diagonal_2] or digit_sum(diagonal_2) != target_sum:
        return
    
    for i in range(5):
        row = read_prime([(r, i) for r in range(5)])
        if not is_prime[row] or digit_sum(row) != target_sum:
            return
        
        column = read_prime([(i, c) for c in range(5)])
        if not is_prime[column] or digit_sum(column) != target_sum:
            return

    ans.append([''.join(map(str, row)) for row in matrix])

def print_answer():
    ans.sort(key=lambda grid: ''.join(grid))

    if not ans:
        print('NONE')

    for i in range(len(ans)):
        for row in ans[i]:
            print(row)
        
        if i < len(ans) - 1:
            print()

def digit_sum(x):
    return sum(map(int, str(x)))

def ith_digit(x, i):
    return int(str(x)[i])

target_sum, upper_left = map(int, input().split())
matrix[0][0] = upper_left

# Sieve of Eratosthenes
p = 2
while p * p < PRIME_LIMIT:
    if is_prime[p]:
        for i in range(p * p, PRIME_LIMIT, p):
            is_prime[i] = False
    p += 1

# NOTE: There's <= 757 primes 5-digits long summing to a particular target_sum
for p in range(10000, PRIME_LIMIT):
    if is_prime[p] and target_sum == digit_sum(p):
        for bitmask in range(1 << 5):
            positions = [10] * 5
            decimal_power = 1

            for bit_index in range(5):
                if bitmask & (1 << bit_index):
                    positions[bit_index] = (p // decimal_power) % 10
                decimal_power *= 10

            choice[tuple(positions[::-1])].append(p)

'''
1   3  3  3   2
8   1  7  2   8
10  4  1  5  10
9   2  7  1   9
2   4  6  5   1
'''
for one in choice[(upper_left, 10, 10, 10, 10)]:
    # one is built from top left to bottom right
    for two in choice[(10, 10, ith_digit(one, 2), 10, 10)]:
        # two is built from top right to bottom left
        for three in choice[(ith_digit(one, 0), 10, 10, 10, ith_digit(two, 4))]:
            # three is built on the first row
            for four in choice[(ith_digit(three, 1), ith_digit(one, 1), 10, ith_digit(two, 1), 10)]:
                # four is built on the second column
                for five in choice[(ith_digit(three, 3), ith_digit(two, 3), 10, ith_digit(one, 3), 10)]:
                    # five is built on the fourth column
                    for six in choice[(ith_digit(two, 0), ith_digit(four, 4), 10, ith_digit(five, 4), ith_digit(one, 4))]:
                        # six is built on the fifth row
                        for seven in choice[(ith_digit(three, 2), 10, ith_digit(one, 2), 10, ith_digit(six, 2))]:
                            # seven is built on the third column
                            for eight in choice[(10, ith_digit(one, 1), ith_digit(seven, 1), ith_digit(two, 3), 10)]:
                                # eight is built on the second row
                                for nine in choice[(10, ith_digit(two, 1), ith_digit(seven, 3), ith_digit(one, 3), 10)]:
                                    # nine is built on the fourth row
                                    for ten in choice[(10, ith_digit(four, 2), ith_digit(one, 2), ith_digit(five, 2), 10)]:
                                        matrix[0][0] = ith_digit(one, 0)
                                        matrix[1][1] = ith_digit(one, 1)
                                        matrix[2][2] = ith_digit(one, 2)
                                        matrix[3][3] = ith_digit(one, 3)
                                        matrix[4][4] = ith_digit(one, 4)
                                        matrix[4][0] = ith_digit(two, 0)
                                        matrix[3][1] = ith_digit(two, 1)
                                        matrix[1][3] = ith_digit(two, 3)
                                        matrix[0][4] = ith_digit(two, 4)
                                        matrix[0][1] = ith_digit(three, 1)
                                        matrix[0][2] = ith_digit(three, 2)
                                        matrix[0][3] = ith_digit(three, 3)
                                        matrix[2][1] = ith_digit(four, 2)
                                        matrix[4][1] = ith_digit(four, 4)
                                        matrix[2][3] = ith_digit(five, 2)
                                        matrix[4][3] = ith_digit(five, 4)
                                        matrix[4][2] = ith_digit(six, 2)
                                        matrix[1][2] = ith_digit(seven, 1)
                                        matrix[3][2] = ith_digit(seven, 3)
                                        matrix[1][0] = ith_digit(eight, 0)
                                        matrix[1][4] = ith_digit(eight, 4)
                                        matrix[3][0] = ith_digit(nine, 0)
                                        matrix[3][4] = ith_digit(nine, 4)
                                        matrix[2][0] = ith_digit(ten, 0)
                                        matrix[2][4] = ith_digit(ten, 4)
                                        add_answer()

print_answer()