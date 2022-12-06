# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:22:47 2022

@author: gape
"""

from collections import Counter, defaultdict
import pandas as pd
import aoc_helper
import re

data = aoc_helper.get_input(5, year=2022)
print('Day 5 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


stacks = defaultdict(list)
stacks2 = defaultdict(list)

d1, d2, _ = data.split('\n\n')

n = 9

for row in d1.split('\n')[:-1]:
    for i in range(n):
        c = row[i*4+1]
        if c != ' ':
            stacks[i+1].insert(0,c )
            stacks2[i+1].insert(0,c )


for move in d2.split('\n'):
    num, a, b = (int(i) for i in re.findall("move (\d+) from (\d+) to (\d+)", move)[0])

    for i in range(num):
        stacks[b].append(stacks[a].pop(-1))
        stacks2[b].append(stacks2[a].pop(-(num-i)))


print("Task 1 answer:", ''.join((stacks[i+1][-1] for i in range(n))))
print("Task 2 answer:", ''.join((stacks2[i+1][-1] for i in range(n))))
