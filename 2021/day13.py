# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:04:09 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(13, year=2021).strip()

print('Day 13 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


def show(new):
    
    m_x = max(new, key=lambda x: x[0])[0]
    m_y = max(new, key=lambda x: x[1])[1]
    canvas = [[' ' for x in range(m_x+1)] for y in range(m_y+1)]

    for x, y in new:
        canvas[y][x] = '#'
    for row in canvas:
        print(''.join(row))
    

dots = []
folds = []
p1 = True
for row in data.split('\n'):
    if row == '':
        p1 = False
        continue
    if p1:
        dots.append(tuple(int(i) for i in row.split(',')))
    else:
        folds.append((row[11], int(row[13:])))
        


new = set(dots)

nums = []
for fold, i in folds:
    old = new
    new = set()
    for x, y in old:
        if fold == 'x':
            if x > i:
                x = i - (x-i)
        if fold == 'y':
            if y > i:
                y = i - (y-i)
        new.add((x,y))
    nums.append(len(new))
    
print("Part 1 answer:", nums[0])
print("Part 2 answer:")
show(new)
