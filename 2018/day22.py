# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 06:05:01 2018

@author: Gape
"""

import numpy as np

def geo(coords, depth):
    x, y = coords
    if x == 0 and y == 0:
        return 0
    elif coords == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
#        return zone[y, x-1] * zone[y-1, x]
        return zone[y][x-1] * zone[y-1][x]
    
    
def erosion(coords, depth):
    return (geo(coords, depth) + depth ) % 20183


possible = {0: (0, 1),
            1: (1, 2),
            2: (2, 0)}
def roll(x, y):
    if y > 0:
        yield x, y-1
    if x > 0:
        yield x-1, y
    if y+1 < target[1] + adder:
        yield x, y+1
    if x+1 < target[0] + adder:
        yield x+1, y


class Section():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.erosion = erosion((x, y), depth)
        self.type = self.erosion%3
        self.value = [None, None, None] # torch, gear, neither
        self.impossible = (self.type+2) % 3
        
        
    def check(self, equip):
        
        current = self.value[equip]
        
        for x, y in roll(self.x, self.y):
            n = zone[y][x]
            for n_equip in range(3):
                if n_equip != n.impossible and n_equip != self.impossible:
                    if n_equip == equip:
                        travel = 1
                    else:
                        travel = 8 # 1 + 7
                    if n.value[n_equip] is None or n.value[n_equip] > current + travel:
                        for other in n.value:
                            if other is not None and other < current + travel + 7:
                                continue
                        n.value[n_equip] = current + travel
                        to_check.add((n, n_equip))
        
    def __mul__(self, other):
        return self.erosion * other.erosion
#depth = 510
#target = 10, 10


depth = 7863
target = 14, 760


zone = np.zeros((target[1]+1, target[0]+1))

for y in range(target[1]+1):
    for x in range(target[0]+1):
        zone[y, x] = erosion((x,y), depth)
        
#zone[target[1], target[0]] = 0

print('Part 1 answer:', (zone%3).sum())

adder = 25

zone = [[None for x in range(target[0]+adder)] for y in range(target[1]+adder)]

for y in range(target[1]+adder):
    for x in range(target[0]+adder):
        zone[y][x] = Section(x, y)
        

n = zone[0][0]
n.value = [0, 0, 0]
to_check = {(n, 0)}

counter = 0
while to_check:
    counter +=1
    if counter % 500000 == 0:
        print('Calculating part 2, queued checks: ', len(to_check), flush=True)
    n, e = to_check.pop()
    n.check(e)

t = zone[target[1]][target[0]]
print('part 2:', min(t.value[0], t.value[1]+7))