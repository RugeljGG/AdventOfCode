# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:14:30 2023

@author: gape
"""

from collections import Counter, defaultdict
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(11, year=2023)
print('Day 11 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]

empty_rows = []
empty_cols = []

for y, row in enumerate(data):
    if '#' not in row:
        empty_rows.append(y)

for x in range(len(row)):
    col = [row[x] for row in data]
    if '#' not in col:
        empty_cols.append(x)


def solve(skip=2):
    galaxies = []
    y_adder = 0
    for y, row in enumerate(data):
        if y in empty_rows:
            y_adder += skip-1
        x_adder = 0
        for x, c in enumerate(row):
            if c == '#':
                galaxies.append(x + x_adder + 1j * (y+y_adder))
            elif x in empty_cols:
                x_adder += skip-1


    lengths = []
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i+1:]:
            d = (g1-g2)
            lengths.append(abs(d.real) + abs(d.imag))

    return sum(lengths)


print("Task 1 answer:", solve(2))
print("Task 2 answer:", solve(1e6))

