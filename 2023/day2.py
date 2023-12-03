# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:58:39 2023

@author: gape
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:57:17 2022

@author: gape
"""

from collections import Counter, defaultdict
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(2, year=2023)
print('Day 2 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [d for d in data.strip().split('\n')]
# data = [int(d) for d in data.strip().split('\n')]

l = []
possible = 0
limit = {'red': 12,
         'green':13,
         'blue': 14,
         }

for i in data:
    a, b = i.split(': ')
    num = int(a[5:])
    games = b.split('; ')
    fail = False
    for g in games:
        for c in g.split(', '):
            amount, color = c.split(' ')
            if limit[color] < int(amount):
                fail = True
                break
        if fail:
            break
    else:
        possible += num

print("Task 1 answer:",  possible)

powers = 0
for i in data:
    a, b = i.split(': ')
    num = int(a[5:])
    games = b.split('; ')
    fewest = Counter()
    for g in games:
        for c in g.split(', '):
            amount, color = c.split(' ')
            fewest[color] = max((int(amount), fewest[color]))

    powers += fewest['green'] * fewest['blue'] * fewest['red']

print("Task 2 answer:", powers)