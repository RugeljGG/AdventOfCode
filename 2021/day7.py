# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 07:46:24 2021

@author: gape
"""

from collections import Counter
import aoc_helper

data = aoc_helper.get_input(7, year=2021).strip()

print('Day 7 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [int(i) for i in data.split(',')]

pos1 = Counter()
pos2 = Counter()

ma = max(data)
mi = min(data)

memory = Counter()


def cost(i):
    if i in memory:
        return memory[i]
    
    if i == 1 or i == 0:
        memory[i] = i
        return i
    else:
        memory[i] = cost(i-1)+i
        return cost(i-1)+i

       
for i, c in enumerate(data):
    for j in range(mi, ma+1):
        pos1[j] += abs(c-j)
        pos2[j] += cost(abs(c-j))
        
        
print("Task 1 answer:", min(pos1.values()))
print("Task 2 answer:", min(pos2.values()))