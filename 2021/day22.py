# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:35:55 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(22, year=2021).strip()

print('Day 22 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


cubes1 = dict()
cubes2 = list()
for row in data.split('\n'):
    r = re.findall("(.+) x=(.*?\d+)..(.*?\d+),y=(.*?\d+)..(.*?\d+),z=(.*?\d+)..(.*?\d+)", row)
    side = r[0][0]
    xmin, xmax, ymin, ymax, zmin, zmax = (int(i) for i in r[0][1:])

    cubes2.append((side, ((xmin, xmax), (ymin, ymax), (zmin, zmax))))
    
    for x in range(max(xmin, -50), min(50, xmax)+1):
        for y in range(max(ymin, -50), min(50, ymax)+1):
            for z in range(max(zmin, -50), min(50, zmax)+1):
                if side == 'on':
                    cubes1[(x,y,z)] = 1
                else:
                    cubes1[(x,y,z)] = 0

print("Part 1 answer:", sum(cubes1.values()))
    

def collision(cube1, cube2):
    
    common = ((max(cube1[0][0], cube2[0][0]),min(cube1[0][1], cube2[0][1])),
              (max(cube1[1][0], cube2[1][0]),min(cube1[1][1], cube2[1][1])),
              (max(cube1[2][0], cube2[2][0]),min(cube1[2][1], cube2[2][1])),
              )
                   
    
    if common[0][0] > common[0][1] or common[1][0] > common[1][1] or common[2][0] > common[2][1]:
        common = None
        new = [cube2]
        return common, new
    else:
        new = []
        if cube2[0][0] < common[0][0]:
            new.append(((cube2[0][0],common[0][0]-1),
                        cube2[1],
                         cube2[2],
                         ))
        if cube2[0][1] > common[0][1]:
            new.append(((common[0][1]+1,cube2[0][1]),
                        cube2[1],
                         cube2[2],
                         ))
        if cube2[1][0] < common[1][0]:
            new.append(((max((cube2[0][0],common[0][0])), min(cube2[0][1],common[0][1])),
                        (cube2[1][0],common[1][0]-1),
                         cube2[2],
                         ))
        if cube2[1][1] > common[1][1]:
            new.append(((max((cube2[0][0],common[0][0])), min(cube2[0][1],common[0][1])),
                        (common[1][1]+1,cube2[1][1]),
                         cube2[2],
                         ))
        if cube2[2][0] < common[2][0]:
            new.append(((max((cube2[0][0],common[0][0])), min(cube2[0][1],common[0][1])),
                       (max((cube2[1][0],common[1][0])), min(cube2[1][1],common[1][1])),
                       (cube2[2][0],common[2][0]-1),
                         ))
        if cube2[2][1] > common[2][1]:
            new.append(((max((cube2[0][0],common[0][0])), min(cube2[0][1],common[0][1])),
                       (max((cube2[1][0],common[1][0])), min(cube2[1][1],common[1][1])),
                       (common[2][1]+1,cube2[2][1]),
                         ))
        return common, new
    
    
def volume(cube):
    if cube is None:
        return 0
    else:
        return abs(cube[0][1]-cube[0][0]+1) * abs(cube[1][1]-cube[1][0]+1) * abs(cube[2][1]-cube[2][0]+1)


turned_on = deque()
to_check = deque(cubes2)



while to_check:
    side, cube2 = to_check.popleft()

    
    new_on = deque()
    current = deque((cube2,))
    while current:
        cube2 = current.popleft()
        for i in range(len(turned_on)):
            cube1 = turned_on.popleft()
            common, new_left = collision(cube2, cube1)
            if side == 'on' and common:
                
                common, new_right = collision(cube1, cube2)
                if len(new_right):
                    new_on.append(common)
                    turned_on.extend(new_left)
                    current.extendleft(new_right)
                else:
                      turned_on.append(cube1)
                break
            else:
                turned_on.extend(new_left)
        else:
            if side == 'on':
                new_on.append(cube2)
    turned_on.extend(new_on)
    print("\rCalculating part 2 - ({:.0%})".format((420-len(to_check))/420), end='')
    
print("\rPart 2 answer:", sum((volume(i) for i in turned_on)))