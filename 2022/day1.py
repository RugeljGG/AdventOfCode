# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:57:17 2022

@author: gape
"""

from collections import Counter
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(1, year=2022)
print('Day 1 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [d for d in data.split('\n')]

s = 0
p = 0

e = []
for i in data:
    if i == '':
        e.append(s)
        s = 0
    else:
        s += int(i)
    pass

print("Task 1 answer:", max(e))
print("Task 2 answer:", sum(pd.Series(e).sort_values().iloc[-3:]))