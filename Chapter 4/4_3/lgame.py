'''
ID: bwliang1
LANG: PYTHON3
TASK: lgame
'''

import sys
from collections import defaultdict
from itertools import permutations

PROBLEM_NAME = 'lgame'
sys.stdin = open(f'{PROBLEM_NAME}.in', 'r')
sys.stdout = open(f'{PROBLEM_NAME}.out', 'w')

letter_map = {
    'q': 7, 'w': 6, 'e': 1, 'r': 2, 't': 2, 'y': 5, 'u': 4, 'i': 1, 'o': 3, 'p': 5,
    'a': 2, 's': 1, 'd': 4, 'f': 6, 'g': 5, 'h': 5, 'j': 7, 'k': 6, 'l': 3,
    'z': 7, 'x': 7, 'c': 4, 'v': 6, 'b': 5, 'n': 2, 'm': 5
}
dictionary = set(w.strip() for w in open('lgame.dict', 'r').readlines()[:-1])
given = input()

score = defaultdict(set)
unique_phrases = set()

for perm in set(permutations(given)):
    for k in range(len(perm) - 1):
        phrase = ''.join(perm[k:])
        unique_phrases.add(phrase)

for phrase in unique_phrases:
    if phrase in dictionary:
        single_score = sum(letter_map[c] for c in phrase)
        score[single_score].add(phrase)
    
    for i in range(3, len(phrase) - 2):
        partial_1, partial_2 = phrase[:i], phrase[i:]
        if partial_1 in dictionary and partial_2 in dictionary:
            double_score = sum(letter_map[c] for c in partial_1) + sum(letter_map[c] for c in partial_2)
            double_phrase = sorted([partial_1, partial_2])
            score[double_score].add(f'{double_phrase[0]} {double_phrase[1]}')

if not score:
    exit(0)

highest_score = max(score)
print(highest_score)
print(*sorted(score[highest_score]), sep='\n')