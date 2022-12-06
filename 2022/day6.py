# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 05:59:13 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import aoc_helper
import re

data = aoc_helper.get_input(6, year=2022)
print('Day 6 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

a = deque()

i = 0
for c in data:
    i += 1
    if len(a) >= 4:
        a.popleft()
    a.append(c)

    if len(set(a)) == 4:
        break

print("Task 1 answer:", i)

i = 0
for c in data:
    i += 1
    if len(a) >= 14:
        a.popleft()
    a.append(c)

    if len(set(a)) == 14:
        break

print("Task 2 answer:", i)