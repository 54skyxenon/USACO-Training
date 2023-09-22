'''
ID: bwliang1
LANG: PYTHON3
TASK: heritage
'''

import sys

PROBLEM_NAME = 'heritage'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

def solve(inorder, preorder):
    assert len(inorder) == len(preorder)

    if len(preorder) < 2:
        return preorder
    
    root = preorder[0]
    pivot = inorder.index(root)
    left = solve(inorder[:pivot], preorder[1:1 + pivot])
    right = solve(inorder[pivot + 1:], preorder[1 + pivot:])
    return f'{left}{right}{root}'

print(solve(input(), input()))