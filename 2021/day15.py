# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:27:25 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
import re

import aoc_helper

data = aoc_helper.get_input(15, year=2021).strip()

print('Day 15 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

class Point:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.total_v = None
        self.neigh = []
                
    def check(self):
        changed = deque()
        for p in self.neigh:
            if p.total_v is None or p.total_v > self.total_v + p.v:
                p.total_v = self.total_v + p.v
                changed.append(p)
        return changed

def solve(data, repeats=1):
    points = dict()
    
    for y, row in enumerate(data.split('\n')):
        for x, c in enumerate(row):
            # points[(x, y)] = Point(x, y, int(c))
            for repeat_x in range(repeats):
                for repeat_y in range(repeats):
                    v = (int(c) + repeat_x + repeat_y)
                    if v > 9:
                        v -= 9
                    x_n = x + repeat_x * len(row)
                    y_n = y + repeat_y * len(row)
                    points[(x_n, y_n)] = Point(x_n, y_n, v)
            
            
    for p in points.values():
        x = p.x
        y = p.y
        if (x+1, y) in points:
            p.neigh.append(points[(x+1, y)])
        if (x, y+1) in points:
            p.neigh.append(points[(x, y+1)])
        if (x-1, y) in points:
            p.neigh.append(points[(x-1, y)])
        if (x, y-1) in points:
            p.neigh.append(points[(x, y-1)])
            
    
    to_check = deque()
    
    points[(0,0)].total_v = 0
    to_check.append(points[(0,0)])
    
    while to_check:
        p = to_check.popleft()
        to_check += p.check()
    
    return max(points.items(), key=lambda x: x[0][0] + x[0][1])[1].total_v

print("Part 1 answer:", solve(data, 1))
print("Part 2 answer:", solve(data, 5))