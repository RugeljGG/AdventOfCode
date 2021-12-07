# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 05:57:40 2021

@author: gape
"""

from collections import Counter
import aoc_helper

data = aoc_helper.get_input(6, year=2021).strip()

print('Day 6 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [int(i) for i in data.split(',')]

def task(days):
    
    m = Counter()
    for d in range(days+9):
        if d < 9:
            m[0] = 0
        else:
            # m[d] = 1 + m[d-9]
            for s in range(((d-9)//7)+1):
                m[d] += 1 + m[d-9-7*s]
            
    s = 0
    for d in data:
        s+= m[days+(8-d)]
        
    return s+len(data)
        

print("Part 1 answer:", task(80))
print("Part 2 answer:", task(256))