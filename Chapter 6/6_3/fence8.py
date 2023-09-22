'''
ID: bwliang1
LANG: PYTHON3
TASK: fence8
'''

# Python solution adapted from: https://suzyz.github.io/2017/08/17/fence8/

import sys
sys.setrecursionlimit(200000)

PROBLEM_NAME = 'fence8'
if '--use-console' not in sys.argv:
    sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
    sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

# Sort boards and rails in ascending order
# If there's a solution with k rails, there's also a solution for the k shortest rails
n = int(input())
boards = [0]
for _ in range(n):
    boards.append(int(input()))
boards.sort()

m = int(input())
rails = [0]
for _ in range(m):
    rails.append(int(input()))
rails.sort()

# Make both a total sum and a prefix sum for rails
sum_boards = sum(boards)
prefix = [0] * (m + 1)

# DFS with iterative deepening
# Iterate through the boards in ascending order, but the rails in descending order
def dfsid(board_idx, rail_idx):
    # We've used all the rails we wanted to use
    if rail_idx <= 0:
        return True

    # Quit if the usuable boards can't match the length of the boards left to use
    if sum(filter(lambda b: b >= rails[1], boards)) < prefix[rail_idx]:
        return False
    
    # If the current rail is the same as the next bigger rail, start at the board we left off at
    start = 1
    if rail_idx < m and rails[rail_idx] == rails[rail_idx + 1]:
        start = board_idx

    # When DFS'ing, make sure to reset any mutations to boards[i] even if you return early
    for i in range(start, n + 1):
        # If the board matches the rail exactly, use it
        if boards[i] == rails[rail_idx]:
            boards[i] = 0
            res = dfsid(1, rail_idx - 1)
            boards[i] = rails[rail_idx]
            return res

        # After that, try your luck with another board
        if boards[i] > rails[rail_idx]:
            boards[i] -= rails[rail_idx]
            res = dfsid(i, rail_idx - 1)
            boards[i] += rails[rail_idx]
            if res:
                return True
        
    return False

# Reduce m to the maximum number of rails we can use before exhausting all board length
for i in range(1, m + 1):
    prefix[i] = prefix[i - 1] + rails[i]
    if prefix[i] > sum_boards:
        m = i - 1
        break

# Binary search for the answer, rather than incrementally
lo = 0
hi = m
while lo < hi:
    mid = (lo + hi + 1) // 2
    if dfsid(1, mid):
        lo = mid
    else:
        hi = mid - 1

print(lo)