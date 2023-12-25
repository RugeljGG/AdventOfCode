# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:02:25 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(10, year=2023)
print('Day 10 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]

types = {'|': [(0, -1), (0, 1)],
         '-': [(1, 0), (-1, 0)],
         'L': [(0, -1), (1, 0)],
         'J': [(0, -1), (-1, 0)],
         '7': [(0, 1), (-1, 0)],
         'F': [(0, 1), (1, 0)],
         }


pipes = dict()
for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '.':
            continue
        if c == 'S':
            start = (x,y)
            c = 'J'
        pipes[(x,y)] = c



to_search = deque()
to_search.append([start, 0])
distances = dict()

while len(to_search):
    (x, y), d = to_search.pop()
    if (x,y) not in pipes:
        print(x,y)
        continue
    else:
        dp = distances.get((x, y))
        if dp is not None and dp < d:
            continue
        distances[(x,y)] = d
        for (xn, yn) in types[pipes[(x,y)]]:
            to_search.append([(x+xn, y+yn), d+1])


count = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) in distances:
            continue
        up = 0
        for yn in range(0, y):
            if (x,yn) in distances and (-1, 0) in types[pipes[(x,yn)]]:
                up += 1
        if up % 2 != 1:
            continue

        down = 0
        for yn in range(y+1, len(data)):
            if (x,yn) in distances and  (-1, 0) in types[pipes[(x,yn)]]:
                down += 1
        if down % 2 != 1:
            continue

        left = 0
        for xn in range(0, x):
            if (xn,y) in distances and  (0, -1) in types[pipes[(xn,y)]]:
                left += 1
        if left % 2 != 1:
            continue


        right = 0
        for xn in range(x+1, len(data[0])):
            if (xn, y) in distances and (0, -1) in types[pipes[(xn,y)]]:
                right += 1
        if right % 2 != 1:
            continue


        count += 1


print("Task 1 answer:", max(distances.values()))
print("Task 2 answer:", count)