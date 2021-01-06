# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 05:58:43 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict, deque
import re

import aoc_helper
#
data = aoc_helper.get_input(22, force=True).strip()
# data = aoc_helper.get_input(22).strip()
print('Day 22 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

decks = data.split('\n\n')

p1 = deque()
for row in decks[0].split('\n')[1:]:
    p1.append(int(row))

p2 = deque()
for row in decks[1].split('\n')[1:]:
    p2.append(int(row))


while len(p1) and len(p2):
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1>c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)


winner = p1 if len(p1) else p2
count = 0
for i, c in enumerate(winner):
    count += (len(winner)-i)*c

print("Part 1 answer:", count)



p1 = deque()
for row in decks[0].split('\n')[1:]:
    p1.append(int(row))

p2 = deque()
for row in decks[1].split('\n')[1:]:
    p2.append(int(row))

def game(p1, p2, d=0):
    states=set()
    while len(p1) and len(p2):
        # print(d)
        # print(p1)
        # print(p2)
        h = '_'.join((str(c) for c in p1)) + '__' + ''.join((str(c) for c in p2))
        if h in states:
            # print("repeated")
            return 1
        else:
            states.add(h)

        c1 = p1.popleft()
        c2 = p2.popleft()

        if c1>len(p1) or c2>len(p2):
            if c1>c2:
                winner = 1
            else:
                winner = 2

        else:
            p1c = deque((p1[i] for i in range(c1)))
            p2c = deque((p2[i] for i in range(c2)))
            winner = game(p1c, p2c, d=d+1)

        # print(winner)
        # print()
        if winner==1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    return 1 if len(p1) else 2

w = game(p1,p2)
winner = p1 if w==1 else p2
count = 0
for i, c in enumerate(p1):
    count += (len(p1)-i)*c

print("Part 2 answer:", count)