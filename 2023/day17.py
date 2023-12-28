# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:24:35 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(17, year=2023)
print('Day 17 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


# data = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533
# """
data = [d for d in data.strip().split('\n')]

blocks = dict()

for y, row in enumerate(data):
    for x, c in enumerate(row):
        blocks[(x + 1j * y)] = int(c)



end = len(data[0])-1 + 1j * (len(data)-1)

dirs = (1j, -1j, 1+0j, -1+0j)

def solve(part=1, sort_steps=5000):
    pos = (0+0j)

    options = deque([(pos, d, 0) for d in dirs])
    saved = dict()
    i = 0
    best = 1e9

    while len(options):

        if i > sort_steps:  # sort options for better performance
            options = deque(sorted(options, key= lambda x: x[2]))
            i = 0
            # print(i, len(saved), len(options), flush=True)

        pos, d, heat = options.popleft()
        if (pos, d) in saved and saved[(pos, d)] <= heat:
            continue
        saved[(pos, d)] = heat

        if pos == end and heat < best:
            best = heat

        for new_d in (d * 1j, d * (-1j) ):
            new_heat = heat
            for l in range(1,4 if part == 1 else 11):
                new_pos = pos+l*new_d
                if new_pos in blocks:
                    new_heat += blocks[new_pos]
                else:
                    break
                if l >= (1 if part == 1 else 4):
                    options.append((new_pos, new_d, new_heat))
                    i += 1

    return best

print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))

