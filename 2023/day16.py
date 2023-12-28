# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:29:24 2023

@author: gape
"""

from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(16, year=2023)
print('Day 16 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = """.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....
# """
data = [d for d in data.strip().split('\n')]

mirrors = dict()

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '.':
            pass
        else:
            mirrors[(x + 1j * y)] = c


def show(energized):
    for y in range(len(data)):
        for x in range(len(data[0])):
            pos = (x + 1j * y)
            if pos in mirrors:
                c = mirrors[pos]
            elif pos in energized:
                c = '#'
            else:
                c = '.'
            print(c, end='')
        print()


def check(start, d):
    lasers = [(start,d)]
    energized = Counter()
    checked = set()
    while len(lasers):
        pos, d = lasers.pop()
        pos += d
        if (pos.real >= 0 and
            pos.real < len(data[0]) and
            pos.imag >= 0 and
            pos.imag < len(data)
            ):
            if (pos, d) in checked:
                continue
            else:
                checked.add((pos, d))
            energized[pos] += 1

            if pos in mirrors:
                m = mirrors[pos]
                if m == '|' and d.real != 0:
                    lasers.append((pos, +1j))
                    lasers.append((pos, -1j))
                    continue
                elif m == '-' and d.imag != 0:
                    lasers.append((pos, +1))
                    lasers.append((pos, -1))
                    continue
                elif m == '\\':
                    d = d.imag + 1j * d.real
                elif m == '/':
                    d = -d.imag -d.real * 1j
            lasers.append((pos, d))
    return energized



to_check = [((-1+1j*y), 1) for y in range(len(data))]
to_check += [((len(data[0])+1j*y), -1) for y in range(len(data))]
to_check += [((x+-1j), 1j) for x in range(len(data))]
to_check += [((x+1j*len(data)), -1j) for x in range(len(data))]

print("Task 1 answer:", len(check((-1+0j),1)))
print("Task 2 answer:", max((len(check(*c)) for c in to_check)))

