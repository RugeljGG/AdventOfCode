# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:37:40 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(18, year=2022)
print('Day 18 input:')
print(data[:100])
print('Total input length: ', len(data))

cubes = dict()
for row in data.strip().split('\n'):
    x,y, z = (int(i) for i in row.split(','))
    cubes[(x,y,z)] = 1


moves = ((1, 0, 0),
         (-1, 0, 0),
         (0, 1, 0),
         (0, -1, 0),
         (0, 0, 1),
         (0, 0, -1),
         )

surface = 0
for x,y,z in cubes:
    c = 6
    for x2,y2,z2 in moves:
        if (x+x2, y+y2, z+z2) in cubes:
            c-=1

    surface +=c


minx = min(cubes, key=lambda x: x[0])[0]-1
maxx = max(cubes, key=lambda x: x[0])[0]+1

miny = min(cubes, key=lambda x: x[1])[1]-1
maxy = max(cubes, key=lambda x: x[1])[1]+1

minz = min(cubes, key=lambda x: x[2])[2]-1
maxz = max(cubes, key=lambda x: x[2])[2]+1


pockets = dict()

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        for z in range(minz, maxz+1):
            if (x,y,z) not in cubes:
                edges = 0
                for  x2,y2,z2 in moves:
                    if (x+x2, y+y2, z+z2) in cubes:
                        edges += 1
                pockets[(x,y,z)] = edges


filled = set()
start = (minx, miny, minz)
steps = deque((start,))
counter = 0
checked = list()
filled.add(start)
while len(steps):

    x,y,z  = steps.popleft()
    checked.append((x,y,z))
    for  x2,y2,z2 in moves:
        new =  (x+x2, y+y2, z+z2)
        if (new[0] < minx or new[0] > maxx or
            new[1] < miny or new[1] > maxy or
            new[2] < minz or new[2] > maxz):
            continue
        if new not in cubes and new not in filled:
            filled.add(new)
            if new in checked:
                raise
            steps.append(new)


surface2 = surface - sum((v for k, v in pockets.items() if k not in filled))

print("Task 1 answer:", surface)
print("Task 2 answer:", surface2)

