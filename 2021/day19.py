# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:57:17 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(19, year=2021).strip()

print('Day 19 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


def rotate_x(coords, n):
    x,y, z = coords
    for i in range(n):
        x, y, z = x, -z, y
    return x, y, z

def rotate_y(coords, n):
    x,y, z = coords
    for i in range(n):
        x, y, z =  -z,y,x
    return x, y, z

def rotate_z(coords, n):
    x,y, z = coords
    for i in range(n):
        x, y, z =  -y,x, z
    return x, y, z


scanners = []
for row in data.strip().split('\n'):
    if "scanner" in row:
        scanners.append([])
        for i in range(24):
            scanners[-1].append([])
    elif row == '':
        continue
    else:
        rots = []
        coords = tuple(int(i) for i in row.split(','))
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if coords not in rots:
                         rots.append(coords)
                    coords = rotate_z(coords, 1)
                coords = rotate_y(coords, 1)
            coords = rotate_x(coords, 1)
        
        for r,rot in enumerate(rots):
            scanners[-1][r].append(rot)
            

correct = scanners[0][0]
# for i in range(len(scanners)-1):
#     s1 = scanners[i][0]
# for j in range(1, len(scanners)):
to_check = scanners[1:]
i_s = 0
moves = []
while to_check:
    i_s+=1
    scanner = to_check.pop(0)
    corr_rot = None
    corr_m = None
    for p1 in correct[::-1]:
        x1, y1, z1 = p1
        for rotation in range(24):
            s2 = scanner[rotation]
            for p2a in s2:
                x2, y2, z2 = p2a
                mx = x2-x1
                my = y2-y1
                mz = z2-z1
                count = 0
                for p2b in s2:
                    x2n = p2b[0] - mx
                    y2n = p2b[1] - my
                    z2n = p2b[2] - mz
                    if (x2n, y2n, z2n) in correct:
                        count += 1
                if count >= 12:
                    corr_rot = rotation
                    corr_m = mx,my,mz
                    moves.append(corr_m)
                    # print(i_s, rotation, mx,my,mz, p1, p2a)
                    for p2b in s2:
                        x2n = p2b[0] - mx
                        y2n = p2b[1] - my
                        z2n = p2b[2] - mz
                        if (x2n, y2n, z2n) not in correct:
                            correct.append((x2n, y2n, z2n))
                    break
            if corr_rot:
                break
        if corr_rot:
            break
    if corr_rot is None:
        to_check.append(scanner)
                
best = 0            
moves.append((0,0,0))
for i in range(len(moves)-1):
    for j in range(i+1,len(moves)):
        m1 = moves[i]
        m2 = moves[j]
        d = abs(m1[0]-m2[0]) + abs(m1[1]-m2[1]) + abs(m1[2]-m2[2])
        if d > best:
            best = d
          
print("Part 1 answer:", len(correct))
print("Part 2 answer:", best)