# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 05:56:34 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict, deque
import re

import aoc_helper
#
data = aoc_helper.get_input(24, force=True).strip()
# data = aoc_helper.get_input(24).strip()
print('Day 24 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


moves = dict(e=(1,0),
             se=(0.5,-0.5),
             sw=(-0.5, -0.5),
             w=(-1,0),
             nw=(-.5,0.5),
             ne=(.5, 0.5))


flips = Counter()
for row in data.split():
    i = 0
    x,y = 0,0
    while i<len(row):
        if row[i:i+2] in moves:
            xn, yn = moves[row[i:i+2]]
            x+= xn
            y+= yn
            i+=2
        else:
            xn, yn = moves[row[i]]
            x+= xn
            y+= yn
            i+=1
    flips[(x,y)] += 1

print("Part 1 answer: ", sum(x%2 for x in flips.values()))

tiles = dict()

for tile in flips.items():
    (x,y), c = tile
    tiles[(x,y)] = c%2


for move in range(100):
    infects = Counter()
    missing = set()
    for (x,y), c in tiles.items():
        if c:
            for xn, yn in moves.values():
                infects[(x+xn, y+yn)] += 1
                if (x+xn, y+yn) not in tiles:
                    missing.add((x+xn, y+yn))

    for tile in missing:
        tiles[tile] = 0

    for tile, c in tiles.items():
        if c and (infects[tile] == 0 or infects[tile] > 2 ):
            tiles[tile] = 0
        elif c == 0 and infects[tile] == 2:
            tiles[tile] = 1

print("Part 2 answer: ", sum(x%2 for x in tiles.values()))
