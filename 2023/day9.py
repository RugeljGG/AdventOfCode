# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:55:11 2023

@author: gape
"""

from collections import Counter, defaultdict
from itertools import cycle
import math
import re

import pandas as pd

import aoc_helper

data = aoc_helper.get_input(9, year=2023)
print('Day 9 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [d for d in data.strip().split('\n')]

count1 = 0
count2 = 0

for row in data:
    s = [int(i) for i in row.split()]
    steps = [s]
    while not (min(s) == max(s) == 0):
        s = [s[i+1]-s[i] for i in range(len(s)-1)]
        steps.append(s)

    s.append(0)

    delta1 = 0
    delta2 = 0

    for s in steps[-2::-1]:
        delta1 = s[-1] + delta1
        delta2 = s[0] - delta2


    count1 += delta1
    count2 += delta2

print("Task 1 answer:", count1)
print("Task 2 answer:", count2)
