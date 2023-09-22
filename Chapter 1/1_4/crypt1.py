'''
ID: bwliang1
LANG: PYTHON3
TASK: crypt1
'''

import sys

PROBLEM_NAME = 'crypt1'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

n = int(input())
digits = list(map(int, input().split()))

def works(path):
    top = int(''.join(path[:3]))
    bottom = int(''.join(path[3:]))
    
    for d in str(bottom):
        partial = int(d) * top
        if not 100 <= partial < 1000 or any(int(p) not in digits for p in str(partial)):
            return False
        
    product = top * bottom
    return 1000 <= product < 10000 and all(int(d) in digits for d in str(product))

def DFS(i, path):
    if i == 5:
        return int(works(path))
    
    ans = 0
    for d in digits:
        path.append(str(d))
        ans += DFS(i + 1, path)
        path.pop()

    return ans

print(DFS(0, []))