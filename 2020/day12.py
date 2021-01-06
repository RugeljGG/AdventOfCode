# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 05:54:15 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(12, force=True).strip()
# data = aoc_helper.get_input(12).strip()
print('Day 12 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


x = 0
y = 0

direction = (1, 0)

moves = {(1, 0): {'L': (0, 1), 'R': (0, -1)},
          (0, 1): {'L': (-1, 0), 'R': (1, 0)},
          (-1, 0): {'L': (0, -1), 'R': (0, 1)},
          (0, -1): {'L': (1, 0), 'R': (-1, 0)}}
         

for row in data.split():
    d = row[0]
    num = int(row[1:])
    if d == 'N':
        y += num
    elif d == 'S' :
        y -= num
    elif d == 'E' :
        x += num
    elif d == 'W' :
        x -= num
    elif d == 'F':
        x += direction[0] * num
        y += direction[1] * num
    elif d == 'R' or d == 'L':
        turns = num // 90
        for t in range(turns):
            direction = moves[direction][d]
        
print("Part 1 answer: ", abs(x) + abs(y))
    
x = 0
y = 0
xw = 10
yw = 1   

for row in data.split():
    d = row[0]
    num = int(row[1:])
    if d == 'N':
        yw += num
    elif d == 'S' :
        yw -= num
    elif d == 'E' :
        xw += num
    elif d == 'W' :
        xw -= num
    elif d == 'F':
        x += xw * num
        y += yw * num
    elif d == 'R' or d == 'L':
        turns = num // 90
        for t in range(turns):
            xw_o = xw
            yw_o = yw
            if d == 'L':
                yw = xw_o
                xw = -yw_o
            elif d == 'R':
                yw = -xw_o
                xw = yw_o
        
print("Part 2 answer: ", abs(x) + abs(y))
    