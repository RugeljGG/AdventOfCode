# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:38:03 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(9, year=2021).strip()

print('Day 9 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

mat = [[int(i) for i in row.strip()] for row in data.split('\n')]


basins = []
s = 0
for y in range(len(mat)):
    for x in range(len(mat[0])):
        v = mat[y][x]
        if (
                (x == 0 or mat[y][x-1] > v)
                and  (y == 0 or mat[y-1][x] > v)
                and  (x == len(mat[0])-1 or mat[y][x+1] > v)
                and  (y == len(mat)-1 or mat[y+1][x] > v)
            ):
            s+=1+v
            basins.append(((x,y), v))

def search(x, y):
    v = mat[y][x]
    # print((x,y), v, end='_')
    if v == 9:
        return set()
    t = set(((x,y),))
    if (x > 0 and mat[y][x-1] > v):
        t.update(search(x-1,y))
    if (y > 0 and mat[y-1][x] > v):
        t.update(search(x,y-1))
    if (x < len(mat[0])-1 and mat[y][x+1] > v):
        t.update(search(x+1,y))
    if (y < len(mat)-1 and mat[y+1][x] > v):
        t.update(search(x,y+1))
    
    return t
    

res = []
for b in basins:
    (x,y), v = b
    t = search(x,y)
    res.append(len(t))
    
i = 1
for r in sorted(res)[-3:]:
    i *= r
    
print("Part 1 answer:", s)
print("Part 2 answer:", i)