# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 05:59:57 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import numpy as np
import re

import aoc_helper

data = aoc_helper.get_input(12, year=2022)
print('Day 12 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


def search(i,j, marks):
    pos = marks[(i, j)]
    height, score = pos
    candidates = deque()
    for move in (-1,0), (1, 0), (0, 1), (0, -1):
        i1 = i+move[0]
        j1 = j+move[1]
        if i1 > mi or j1 > mj or i1 < 0 or j1 < 0:
            continue

        h1, s1 = marks[(i1, j1)]
        if (height-h1)<=1:
            if s1 is None or s1 > score+1:
                marks[(i1, j1)][1] = score+1
                candidates.append((i1, j1))

    return candidates

marks = dict()
start = None
end = None

for i, row in enumerate(data.strip().split()):
    for j, c in enumerate(row):
        if c == 'S':
            start = i,j
            c = 'a'
        elif c == 'E':
            end = i, j
            c = 'z'
        marks[i,j] = [ord(c)-97, None]


mi = max(marks, key=lambda x: x[0])[0]
mj = max(marks, key=lambda x: x[1])[1]

marks[end][1] = 0
candidates = deque([end])
best = None

while len(candidates):
    i, j = candidates.popleft()
    if marks[i, j][0] == 0:
        if best is None or  marks[i, j][1] < best:
            best =  marks[i, j][1]
    new = search(i, j, marks)
    for n in new:
        if n not in candidates:
            candidates.append(n)

print("Task 1 answer:", marks[start][1])
print("Task 2 answer:", best)