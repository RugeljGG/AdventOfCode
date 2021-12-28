# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 05:57:46 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
import re

import aoc_helper

data = aoc_helper.get_input(25, year=2021).strip()

print('Day 25 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


c_east = dict()
c_down = dict()
c_all = dict()
for y, row in enumerate(data.split('\n')):
    for x, c in enumerate(row):
        if c != '.':
            if c == '>':
                c_east[(x,y)] = c
            if c == 'v':
                c_down[(x,y)] = c
            c_all[(x,y)] = c

my = max(c_all, key=lambda x: x[1])[1]
mx = max(c_all, key=lambda x: x[0])[0]

step = 0
moved = 1
while moved>0:
    c_e_n = dict()
    c_d_n = dict()
    c_n = dict()
    moved = 0
    for (x,y), c in c_east.items():
        y_n = y
        if x<mx:
            x_n = x+1
        else:
            x_n = 0
        if (x_n, y_n) in c_all:
            c_n[(x,y)] = c
            c_e_n[(x, y)] = c
        else:
            c_n[(x_n, y_n)] = c
            c_e_n[(x_n, y_n)] = c
            moved+=1
            
    for (x,y), c in c_down.items():
        if c == 'v':
            x_n = x
            if y<my:
                y_n = y+1
            else:
                y_n = 0
        if (x_n, y_n) in c_down or (x_n, y_n) in c_e_n:
            c_n[(x,y)] = c
            c_d_n[(x,y)] = c
        else:
            c_n[(x_n, y_n)] = c
            c_d_n[(x_n, y_n)] = c
            moved+=1
    cucs = c_n
    c_east = c_e_n
    c_down = c_d_n
    step+=1
            
print("Part 1 answer:", step)