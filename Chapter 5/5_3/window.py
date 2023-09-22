'''
ID: bwliang1
LANG: PYTHON3
TASK: window
'''

import sys
from functools import reduce

PROBLEM_NAME = 'window'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

class ListNode():
    ''' For a simple doubly linked list implementation. '''
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

commands = [line.strip() for line in sys.stdin.readlines()]

bounds = dict()
node = dict()
nodes_head = ListNode('#')
nodes_tail = ListNode('$')
nodes_head.nxt = nodes_tail
nodes_tail.prev = nodes_head

def split_off(initial, affected):
    x11, y11, x21, y21 = initial
    x12, y12, x22, y22 = affected

    intersection = (max(x11, x12), max(y11, y12), min(x21, x22), min(y21, y22))

    # nothing in common
    if intersection[0] >= intersection[2] or intersection[1] >= intersection[3]:
        return [initial]
    
    new_rectangles = []

    # carve out top
    if intersection[3] < initial[3]:
        new_rectangles.append((initial[0], intersection[3], initial[2], initial[3]))
        
    # carve out bottom
    if intersection[1] > initial[1]:
        new_rectangles.append((initial[0], initial[1], initial[2], intersection[1]))
    
    # carve out left
    if intersection[0] > initial[0]:
        new_rectangles.append((initial[0], intersection[1], intersection[0], intersection[3]))

    # carve out right
    if intersection[2] < initial[2]:
        new_rectangles.append((intersection[2], intersection[1], initial[2], intersection[3]))

    return new_rectangles

def get_area(bound):
    return (bound[2] - bound[0]) * (bound[3] - bound[1])

for command in commands:
    args = command[2:-1]
    if command.startswith('w'):
        ''' Puts new window on top. '''
        tokens = args.split(',')
        I = tokens[0]
        x, y, X, Y = map(int, tokens[1:])
        x1, x2 = min(x, X), max(x, X)
        y1, y2 = min(y, Y), max(y, Y)
        bounds[I] = (x1, y1, x2, y2)
        node[I] = ListNode(I, prev=nodes_head, nxt=nodes_head.nxt)
        nodes_head.nxt.prev = node[I]
        nodes_head.nxt = node[I]
    elif command.startswith('t'):
        ''' Moves window to top. '''
        I = args
        prev, nxt = node[I].prev, node[I].nxt
        prev.nxt = nxt
        nxt.prev = prev
        node[I].prev = nodes_head
        node[I].nxt = nodes_head.nxt
        node[I].nxt.prev = node[I]
        node[I].prev.nxt = node[I]
    elif command.startswith('b'):
        ''' Moves window to bottom. '''
        I = args
        prev, nxt = node[I].prev, node[I].nxt
        prev.nxt = nxt
        nxt.prev = prev
        node[I].prev = nodes_tail.prev
        node[I].nxt = nodes_tail
        node[I].nxt.prev = node[I]
        node[I].prev.nxt = node[I]
    elif command.startswith('d'):
        ''' Deletes a window. '''
        I = args
        prev, nxt = node[I].prev, node[I].nxt
        prev.nxt = nxt
        nxt.prev = prev
        del node[I]
        del bounds[I]
    elif command.startswith('s'):
        I = args
        
        ptr = nodes_head.nxt
        cut_off = []
        while ptr.val != I:
            cut_off.append(bounds[ptr.val])
            ptr = ptr.nxt

        rectangles = reduce(lambda remains, cover: sum([split_off(patch, cover) for patch in remains], []), cut_off, [bounds[I]])
        ratio = sum(map(get_area, rectangles)) / get_area(bounds[I])
        print('{:.3f}'.format(100 * ratio))
    else:
        raise ValueError('Invalid command!')