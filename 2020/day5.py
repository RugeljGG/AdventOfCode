# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 05:54:36 2020

@author: gape
"""

import aoc_helper
import re

data = aoc_helper.get_input(5, force=True)

print('Day 5 input (first 5 lines):')
print('\n'.join(data.split('\n')[:5]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

best = 0
ids = set()
for row in data.split('\n')[:-1]:
    i = 0
    j = 127
    for c in row[:7]:
        if c == 'F':
            j = (j+i)//2
        else:
            i = (j+i)//2+1
        # print(c, i, j)
    rown = j
    
    ir = 0
    jr = 7
    for c in row[-3:]:
        if c == 'L':
            jr = (jr+ir)//2
        else:
            ir = (jr+ir)//2+1
    coln = ir
    
    # print(row)
    # print(rown, i, j)
    # print(coln, ir, jr)
    
    sid = rown * 8 + coln
    if sid>best:
        best = sid
    ids.add(sid)
    
print('Part 1 answer: ', best)

last = 0
for i in range(1, best):
    if i not in ids:
        if last == i-1:
            last = i
        else:
            print('Part 2 answer: ', i)
            break
        
        