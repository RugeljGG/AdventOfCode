# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 07:38:30 2021

@author: gape
"""

from collections import Counter
import aoc_helper

data = aoc_helper.get_input(5, year=2021, force=True).strip()

print('Day 5 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = data.split('\n')


horizontal = []
vertical = []
diagonal = []
for row in data:
    entry, exit = row.split(' -> ')
    entry = list(int(i) for i in entry.split(','))
    exit = list(int(i) for i in exit.split(','))
    if entry[1] == exit[1]:
        horizontal.append((entry, exit))
    elif entry[0] == exit[0]:
        vertical.append((entry, exit))      
    else:
        diagonal.append((entry, exit))
        
taken = Counter()

for l in horizontal:
    y = l[0][1]
    xs = min((l[0][0], l[1][0]))
    xe = max((l[0][0], l[1][0]))
    for x in range(xs, xe+1):
        taken[(x,y)] += 1
        
for l in vertical:
    x = l[0][0]
    ys = min((l[0][1], l[1][1]))
    ye = max((l[0][1], l[1][1]))
    for y in range(ys, ye+1):
        taken[(x,y)] += 1
        
    
s = 0
for i in taken.values():
    if i>1:
        s+=1
        
        
print("Part 1 answer:", s)

for l in diagonal:
    xs = l[0][0]
    xe = l[1][0]
    xp = 1 if xs < xe else -1
    ys = l[0][1]
    ye = l[1][1]
    yp = 1 if ys < ye else -1
        
    for i in range(abs(xe-xs)+1):
        taken[(xs+i*xp,ys+i*yp)] += 1
        
s = 0
for i in taken.values():
    if i>1:
        s+=1
        
print("Part 2 answer:", s)