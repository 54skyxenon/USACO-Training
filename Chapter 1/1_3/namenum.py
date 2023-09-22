'''
ID: bwliang1
LANG: PYTHON3
TASK: namenum
'''

import sys

PROBLEM_NAME = 'namenum'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

pad = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y']
}

num = input()
names = set(open('dict.txt', 'r').read().splitlines())
outputted = False

def DFS(i, name):
    if i == len(num):
        if name in names:
            print(name)
            global outputted
            outputted = True
        return
    
    for letter in pad[num[i]]:
        DFS(i + 1, name + letter)

DFS(0, '')
if not outputted:
    print('NONE')