# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 05:55:41 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(10, force=True).strip()
print('Day 10 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

data = [int(i) for i in data.split()]

data = sorted(data)

v = 0
v1 = 0
v2 = 0

for d in data:
    if d-v == 1:
        v1 +=1
    else:
        v2 += 1
    v = d
    
v2 += 1

print("Part 1 answer: ", v1*v2)

vsi = Counter()

vsi[0] = 1
data2 = [0]+data
for i, d in enumerate([0]+data):
    ds = []
    for d2 in data2[i+1:i+4]:
        if d2-d <= 3:
           vsi[d2] += vsi[d]
           

print("Part 2 answer: ", vsi[max(data2)])