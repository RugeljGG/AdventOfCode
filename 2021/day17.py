# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 07:35:16 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import prod
import re

import aoc_helper

data = aoc_helper.get_input(17, year=2021).strip()

print('Day 17 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

x_l = 277, 318
y_l = -92, -53

# x_l = 20, 30
# y_l = -10, -5

def test(xv, yv, x_l, y_l):
    x = 0
    y = 0
    y_m = 0
    while x <= x_l[1] and y >= y_l[0]:
        x+= xv
        y+= yv
        # print(x,y)
        yv -= 1
        if xv > 0:
            xv -=1
        elif xv < 0:
            xv += 1
        if y > y_m:
            y_m = y
        
        if x >= x_l[0] and  x <= x_l[1] and y >= y_l[0] and y <= y_l[1]:
            break
    else:
        return False
    return y_m

best = 0
num = 0
for x in range(1,x_l[1]+1):
    for y in range(y_l[0], abs(y_l[0])+1):
        n = test(x, y, x_l, y_l)
        if n is not False:
            num += 1
            if n > best:
                best = n
        
print("Part 1 answer:", best)
print("Part 2 answer:", num)