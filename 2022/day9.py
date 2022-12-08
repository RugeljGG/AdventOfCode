# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:40:03 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import numpy as np
import re

import aoc_helper

data = aoc_helper.get_input(8, year=2022)
print('Day 8 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()



trs = []
for row in data.split():
    trs.append(list((int(i) for i in row)))

trs = np.array(trs)

def task1():
    num = 0
    n = len(trs)
    m = len(trs[0])
    for row in range(n):
        for col in range(m):
            tr = trs[row, col]
            if col == 0 or row == 0 or col == m-1 or row == n -1:
                num +=1
            elif max(trs[row,:col]) < tr or max(trs[row,col+1:]) < tr:
                num += 1
            elif max(trs[:row,col]) < tr or max(trs[row+1:,col]) < tr:
                num += 1


    num = 0


def search(line, h):
    if len(line) == 0:
        return 0
    elif line[0] >= h:
        return 1
    else:
        return search(line[1:], h) + 1

n = len(trs)
m = len(trs[0])
best = 0
for row in range(n):
    for col in range(m):
        tr = trs[row, col]
        score = search(trs[row, col+1:], tr) * search(trs[row, :col][::-1], tr) *  search(trs[:row, col][::-1], tr) * search(trs[row+1:, col], tr)
        if score > best:
            best = score