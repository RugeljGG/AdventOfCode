# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:24:45 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(23, year=2022)
print('Day 23 input:')
print(data[:100])
print('Total input length: ', len(data))


# data ="""....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#.."""

def show(elves, minx=-3, maxx=10, miny=-2, maxy=10):
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx, maxx+1):
            # if (x,y) in elves:
            #     c = '{:02d} '.format(elves.get((x,y)))
            # else:
            #     c = ' . '
            if (x,y) in elves:
                c = '#'
            else:
                c = '.'
            row.append(c)
        print(''.join(row))
    print()


order = deque(('N', 'S', 'W', 'E'))
elves = dict()
counter = 0
for y, row in enumerate(data.strip().split('\n')):
    for x, c in enumerate(row):
        if c == '#':
            elves[(x,y)] = counter
            counter += 1



neigh = {'N':((-1, -1), (0, -1), (1, -1)),
         'S': ((-1, 1), (0, 1),   (1, 1)),
         'W': ((-1, -1), (-1, 0), (-1, 1)),
         'E': ((1, -1), (1, 0),   (1, 1)),
         }

moves = {'N': (0, -1),
        'S': (0, 1),
        'W': (-1, 0),
        'E': (1, 0),
        }
all_neigh = set((i for v in neigh.values() for i in v))
i = 0
while True:
    i += 1
    proposals = defaultdict(list)
    for elf in elves:
        for n in all_neigh:
            x = elf[0]+n[0]
            y = elf[1]+n[1]
            if (x, y) in elves:
                break
        else:
            continue
        for o in order:
            for n in neigh[o]:
                x = elf[0]+n[0]
                y = elf[1]+n[1]
                if (x, y) in elves:
                    break
            else:
                move = moves[o]
                x = elf[0]+move[0]
                y = elf[1]+move[1]
                proposals[(x,y)].append(elf)
                break

    moved = False
    for p, v in proposals.items():
        if len(v) == 1:
            moved = True
            c = elves.pop(v[0])
            elves[p] = c
    if not moved:
        break

    order.append(order.popleft())

    if i == 10:
        min_x = min(elves, key=lambda x: x[0])[0]
        max_x = max(elves, key=lambda x: x[0])[0]
        min_y = min(elves, key=lambda x: x[1])[1]
        max_y = max(elves, key=lambda x: x[1])[1]

        print("Task 1 answer:", (max_y-min_y+1) * (max_x-min_x+1) - len(elves))


print("Task 2 answer:", i)


