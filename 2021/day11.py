# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:37:14 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(11, year=2021).strip()

print('Day 11 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

def return_coords(x, y, x_lim=10, y_lim=10):
    coords = []
    if x > 0 and y>0:
        coords.append((x-1, y-1))
    if y > 0:
        coords.append((x, y-1))
    if x < x_lim-1 and y>0:
        coords.append((x+1, y-1))
    if x < x_lim-1:
        coords.append((x+1, y))
    if x < x_lim-1 and y < y_lim -1:
        coords.append((x+1, y+1))     
    if  y < y_lim -1:
        coords.append((x, y+1))
    if x > 0 and y < y_lim -1:
        coords.append((x-1, y+1)) 
    if x > 0:
        coords.append((x-1, y))

    return coords
 

def show(octi, i):
    print("Step", i)
    for y in range(10):
        print(''.join((str(octi[(x,y)]) for x in range(10))))
    print()
    
    

octi = dict()

for j, row in enumerate(data.split('\n')):
    for i, v in enumerate(row):
        octi[(i, j)] = int(v)
        
steps = 1000
c = 0

# show(octi, 0)
for s in range(steps):
    flashes = []
    flashed = []
    for (x,y) in octi.keys():
        octi[(x, y)] += 1
        if octi[(x, y)] > 9:
            flashes.append((x,y))
    
    # print(flashes)
    while len(flashes):
        x,y = flashes.pop()
        if (x,y) not in flashed:
            c += 1
            flashed.append((x,y))
            for (x2, y2) in return_coords(x,y):
                octi[(x2, y2)] += 1
                if octi[(x2, y2)] > 9 and (x2,y2) not in flashed:
                    flashes.append((x2,y2))
    for (x,y) in flashed:
        octi[(x, y)] = 0
    
    if s == 99:
        print(c)
    
    if len(flashed) == 100:
        print(s)
        break
        
