# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 06:14:08 2022

@author: gape
"""

from collections import Counter
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(3, year=2022)
print('Day 3 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]

s = 0
for bag in data:
    c1 = bag[:len(bag)//2]
    c2 = bag[len(bag)//2:]
    for c in c1:
        if c in c2:
            v = ord(c) - 64 +26 if c.isupper() else ord(c) - 96
            s += v
            break
        else:
            continue
        break

print("Task 1 answer:", s)



s = 0
for i, bag in enumerate(data):
    if i % 3 == 0:
        counts = Counter()
    for c in set(bag):
        counts[c] += 1

    if i % 3 == 2:
        for k, v in counts.items():
            if v == 3:
                v = ord(k) - 64 +26 if k.isupper() else ord(k) - 96
                s += v

print("Task 2 answer:",s)