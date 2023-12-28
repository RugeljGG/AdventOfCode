# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:01:29 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(18, year=2023)
print('Day 18 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


# data = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)
# """


def slow():  # old part 1, not useful for part 2
    pos = (0+0j)

    holes = dict()
    holes[pos] = '#'
    for row in data:
        d, l, c = re.findall(pattern, row)[0]
        l = int(l)

        for i in range(l):
            pos += dirs[d]
            holes[pos] = c

    filled = set()

    fill_start = (1+1j)
    fill_options = deque([fill_start])
    while len(fill_options):
        pos = fill_options.popleft()
        if pos in holes or pos in filled:
            continue

        filled.add(pos)
        for d in dirs.values():
            fill_options.append(pos+d)


    print(len(holes) + len(filled))


data = [d for d in data.strip().split('\n')]
pattern = "(.) (\d+) \((#.*?)\)"

dirs = dict(R=1+0j,
            D=1j,
            L=-1+0j,
            U=-1j,
            )


def solve(part=1):
    pos = (0+0j)

    size = 0
    length = 0

    for row in data:
        d, l, c = re.findall(pattern, row)[0]

        if part == 1:
            d = dirs[d]
            l = int(l)

        else:
            d = list(dirs.values())[int(c[-1], 16)]
            l = int(c[1:-1], 16)

        size -= d.real * pos.imag * l
        pos += d *l
        length += l

    return size + length / 2 + 1  # integral + polovico debeline + 1 (koti)


print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))

