# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 05:56:42 2022

@author: gape
"""

from collections import Counter
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(2, year=2022)
print('Day 2 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


# data = """A Y
# B X
# C Z"""
data = [d for d in data.strip().split('\n')]

mapper = {'X': 1,
          'Y': 2,
          'Z': 3,}

mapper_w = {'A': 'Y',
            'B': 'Z',
            'C': 'X',}

mapper_l = {'A': 'Z',
            'B': 'X',
            'C': 'Y',}

mapper_t = {'A': 'X',
            'B': 'Y',
            'C': 'Z',}

mapper_a = {'A': 'R',
            'B': 'P',
            'C': 'S',}

mapper_b = {'X': 'R',
            'Y': 'P',
            'Z': 'S',}

s = 0
for row in data:
    a, b = row.split(' ')
    if mapper_t[a] == b:
        s += 3
    elif mapper_w[a] == b:
        s +=6
    else:
        s+= 0
    s+= mapper[b]

print("Task 1 answer:", s)

s = 0
for row in data:
    a, b = row.split(' ')
    if b == 'X':
        c = mapper_l[a]
    if b == 'Y':
        c = mapper_t[a]
        s+=3
    if b == 'Z':
        c = mapper_w[a]
        s+=6
    s+= mapper[c]

print("Task 2answer:", s)