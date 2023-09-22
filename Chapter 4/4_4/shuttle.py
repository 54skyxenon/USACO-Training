'''
ID: bwliang1
LANG: PYTHON3
TASK: shuttle
'''

import sys

PROBLEM_NAME = 'shuttle'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

OUTPUT_LENGTH = 20

n = int(input())
start = f"{'W' * n}_{'B' * n}"
target = start[::-1]

def shift_left(board):
    board = list(board)
    spot = board.index('_')

    if spot < len(board) - 1 and board[spot + 1] == 'B':
        board[spot], board[spot + 1] = board[spot + 1], board[spot]
    
    return ''.join(board)

def hop_left(board):
    board = list(board)
    spot = board.index('_')

    if spot < len(board) - 2 and board[spot + 1] + board[spot + 2] == 'WB':
        board[spot], board[spot + 2] = board[spot + 2], board[spot]
    
    return ''.join(board)

def shift_right(board):
    board = list(board)
    spot = board.index('_')

    if spot > 0 and board[spot - 1] == 'W':
        board[spot], board[spot - 1] = board[spot - 1], board[spot]
    
    return ''.join(board)

def hop_right(board):
    board = list(board)
    spot = board.index('_')

    if spot > 1 and board[spot - 2] + board[spot - 1] == 'WB':
        board[spot], board[spot - 2] = board[spot - 2], board[spot]
    
    return ''.join(board)

def transform(path):
    return [1 + state.index('_') for state in path]

best_solution = []

def DFS(curr, path):
    if curr == target:
        path = path[::-1][1:]
        if not best_solution or transform(path) < transform(best_solution):
            best_solution.clear()
            best_solution.extend(path)
        
        return

    # If we can hop (i.e. _WB -> BW_ or BW_ -> _WB), do so as our action on this step
    hl, hr = hop_left(curr), hop_right(curr)
    if hl not in path or hr not in path:
        if hl not in path:
            path.append(hl)
            DFS(hl, path)
            path.pop()

        if hr not in path:
            path.append(hr)
            DFS(hr, path)
            path.pop()
        
        return

    # Otherwise, we try the shifts
    sl, sr = shift_left(curr), shift_right(curr)
    if sl not in path:
        path.append(sl)
        DFS(sl, path)
        path.pop()
    
    if sr not in path:
        path.append(sr)
        DFS(sr, path)
        path.pop()

    # REMARK: This limits the branching factor to 2 => 2^25 is passable

DFS(start, [start])
for i in range(0, len(best_solution), OUTPUT_LENGTH):
    print(' '.join(map(str, transform(best_solution[i:i + OUTPUT_LENGTH]))))