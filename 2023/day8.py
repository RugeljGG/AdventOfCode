# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:32:49 2023

@author: gape
"""

from collections import Counter, defaultdict
from itertools import cycle
import math
import re

import pandas as pd

import aoc_helper

data = aoc_helper.get_input(8, year=2023)
print('Day 8 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]


paths = dict()

pattern = "(.*?) = \((.*?), (.*?)\)"
starting = []
for row in data[2:]:
    r = re.findall(pattern, row)[0]
    paths[r[0]] = r[1], r[2]
    if r[0][-1] == 'A':
        starting.append(r[0])


cur = 'AAA'

count = 0
lr = cycle(data[0])
while cur != 'ZZZ':
    turn = next(lr)
    count += 1
    if turn == 'L':
        cur = paths[cur][0]
    elif turn == 'R':
        cur = paths[cur][1]
    else:
        print("ojoj")

print("Task 1 answer:", count)


finishes = []
for cur in starting:
    count = 0
    lr = cycle(data[0])
    while cur[-1] != 'Z':
        turn = next(lr)
        count += 1
        if turn == 'L':
            cur = paths[cur][0]
        elif turn == 'R':
            cur = paths[cur][1]
    finishes.append(count)

print("Task 2 answer:", math.lcm(*finishes))
