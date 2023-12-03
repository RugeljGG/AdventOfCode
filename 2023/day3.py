# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:36:47 2023

@author: gape
"""

from collections import Counter, defaultdict
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(3, year=2023)
print('Day 3 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

data = [d for d in data.strip().split('\n')]



correct = []
gears = defaultdict(list)
for row_n, row in enumerate(data):
    i = 0
    while i < len(row):
        j = i
        num = ''
        while j < len(row) and row[j].isdigit():
            num += row[j]
            j += 1
        if num != '':
            works = False
            for ax in range(i-1, j+1):
                if ax < 0 or ax >= len(row):
                    continue
                for ay in range(row_n-1, row_n+2):
                    if ay < 0 or ay >= len(data):
                        continue
                    ac = data[ay][ax]
                    if not ac.isdigit() and ac != '.':
                        works = True
                    if ac == '*':
                        gears[(ax, ay)].append(int(num))
                        break
            if works:
                correct.append(int(num))
        i = j+1

answer = 0
for g in gears.values():
    if len(g) == 2:
        answer += g[0] * g[1]

print("Task 1 answer:", sum(correct))
print("Task 2 answer:", answer)

