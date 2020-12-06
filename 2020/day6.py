# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 05:57:47 2020

@author: gape
"""

from collections import Counter
import aoc_helper
data = aoc_helper.get_input(6, force=True).strip()

print('Day 6 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

count = 0
for g in data.split('\n\n'):
    gr = set()
    for p in g.split():
        for c in p:
            gr.add(c)
    count+=len(gr)

print("Part 1 answer: ", count)

count = 0
for g in data.split('\n\n'):
    num = 0
    gr = Counter()
    for p in g.split():
        for c in p:
            gr[c] += 1
        num+=1
    for k, v in gr.items():
        if v == num:
            count+=1
    
print("Part 2 answer: ", count)