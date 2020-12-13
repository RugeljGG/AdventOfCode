# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 05:57:14 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(13, force=True).strip()
# data = aoc_helper.get_input(12).strip()
print('Day 13 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

ts = int(data.split('\n')[0])

data0 = data.split('\n')[1].split(',')

buses = []

for b in data0:
    if b == 'x':
        continue
    else:
        buses.append(int(b))

best = ts
best_b = None
for b in buses:
    t = ts // b
    wait = b * (t+1) - ts
    if wait < best:
        best = wait
        best_b = b
        
print("Part 1 answer: ", best_b * best)


buses = []
highest = 0, 0
for i,b in enumerate(data0):
    if b == 'x':
        continue
    else:
        if int(b) > highest[1]:
            highest = i, int(b)
        buses.append([i, int(b)])

sol = 0, 1
for m, b in sorted(buses, key=lambda x: x[1], reverse=True)[1:]:
    i = sol[0]
    while True:
        i += sol[1]
        if (highest[1] * i - highest[0] + m) % b == 0:
            break
    sol = i, sol[1] * b
    
print("Part 2 answer: ", sol[0] * highest[1] - highest[0])