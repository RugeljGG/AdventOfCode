# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:52:07 2023

@author: gape
"""

from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(14, year=2023)
print('Day 14 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """


data = [d for d in data.strip().split('\n')]

def task1():
    rocks = dict()
    for y,row in enumerate(data):
        for x,c in enumerate(row):
            if c in ('#', 'O'):
                rocks[(x, y)] = c

    order = sorted(rocks)

    new = dict()
    cols = Counter()
    load = 0
    for x, y in order:

        v = rocks[(x,y)]
        if v == '#':
            cols[x] = y+1
            new[(x,y)] = v

        else:
            load += len(data) - cols[x]
            new[(x,cols[x])] = v
            cols[x] += 1

    return load




def task2():
    rocks = []
    for y,row in enumerate(data):
        for x,c in enumerate(row):
            if c in ('#', 'O'):
                rocks.append(((x,y), c))

    memory = dict()
    new = rocks
    c = 0
    while c < 1e9:
        for r in range(4):
            rocks = new
            new = []
            cols = Counter()
            for (x,y), v in rocks:

                if v == '#':
                    cols[x] = y+1
                    new.append(((len(data)-y-1, x), v))

                else:
                    new.append(((len(data)-cols[x]-1,x), v))
                    cols[x] += 1

            new = tuple(sorted(new))

        canvas = [['.' for x in range(len(data[0]))] for y in range(len(data))]


        if new in memory:
            cycles = (c - memory[new])
            if (1e9-c) % cycles == 1:
                break
        else:
            memory[new] = c
        c += 1

    load = 0
    for (x,y), rock in new:
        canvas[y][x] = rock
        if rock == 'O':
            load += len(data) - y
    return load

print("Task 1 answer:", task1())
print("Task 2 answer:", task2())