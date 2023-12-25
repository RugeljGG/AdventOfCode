# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:29:43 2023

@author: gape
"""


from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(13, year=2023)
print('Day 13 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """

data = [d.strip().split('\n') for d in data.strip().split('\n\n')]

def solve(group, part=1):
    margin = 0 if part == 1 else 1
    for m_col in range(1, len(group[0])):
        wrong = 0
        for y, row in enumerate(group):
            for x in range(m_col):
                x_m = 2*m_col-x-1
                if x_m >= len(group[0]):
                    continue
                if row[x] != row[x_m]:
                    wrong += 1
                    if wrong > margin:
                        break
            else:
                continue
            break
        else:
            if wrong == margin:
                return m_col

    for m_row in range(1, len(group)):
        wrong = 0
        for y in range(m_row):
            y_m = 2*m_row-y-1
            if y_m >= len(group):
                continue
            for x in range(len(group[0])):
                if group[y][x] != group[y_m][x]:
                    wrong += 1
                    if wrong > margin:
                        break
            else:
                continue
            break
        else:
            if wrong == margin:
                return m_row * 100



print("Task 1 answer:", sum((solve(g, 1) for g in data)))
print("Task 2 answer:", sum((solve(g, 2) for g in data)))


