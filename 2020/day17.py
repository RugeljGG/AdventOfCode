# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 05:56:30 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(17, force=True).strip()
# data = aoc_helper.get_input(17).strip()
print('Day 17 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

class Cube:
    def __init__(self, x,y,z,w):
        self.active = 0
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.count = 0
        self.active_old = 0
    
    def infect(self, cubes, part=1):
        if part == 1:
            w_s, w_e = 0, 1
        elif part == 2:
            w_s, w_e = self.w-1, self.w+2
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                for z in range(self.z-1, self.z+2):
                    for w in range(w_s, w_e):
                        if self.x == x and self.y == y and self.z == z and self.w == w:
                            continue
                        else:
                            if (x,y,z,w) not in cubes:
                                cubes[(x,y,z,w)] = Cube(x,y,z,w)
                            cubes[(x,y,z,w)].count += 1
    

def show(active):
    xs, xe = min(active, key=lambda x: x[0])[0], max(active, key=lambda x: x[0])[0]+1
    ys, ye = min(active, key=lambda x: x[1])[1], max(active, key=lambda x: x[1])[1]+1
    zs, ze = min(active, key=lambda x: x[2])[2], max(active, key=lambda x: x[2])[2]+1
    ws, we = min(active, key=lambda x: x[3])[3], max(active, key=lambda x: x[3])[3]+1
    for w in range(ws, we):
        for z in range(zs, ze):
            print("z={},w={}".format(z,w))
            for y in range(ys, ye):
                for x in range(xs, xe):
                    if (x,y,z,w) not in active:
                        print('.',end='')
                    else:
                        print('#', end='')
                print()
            print()


def run(data, part=1, verbose=False):
    cubes = dict()
    active = dict()    
    z = 0
    w = 0
    for y, row in enumerate(data.split()):
        for x, c in enumerate(row):
            cube = Cube(int(x),int(y),z,w)
            cubes[(x,y,z,w)] = cube
            if c == '#':
                cube.active = 1
                active[(x,y,z,w)] = cube
    for r in range(6):
        if verbose:
            print("Runda", r, len(active))
            show(active)
        for cube in cubes.values():
            cube.count = 0
            cube.active_old = cube.active
        
        for cube in active.values():
            cube.infect(cubes, part=part)
            
        active = dict()
        for cube in cubes.values():
            if ((not cube.active_old and cube.count == 3)
            or cube.active_old and (cube.count == 2 or cube.count == 3)):
                cube.active = 1
                active[(cube.x, cube.y, cube.z, cube.w)] = cube
            else:
                cube.active = 0
    return len(active)


print("Part 1 answer: ", run(data, part=1))
print("Part 2 answer: ", run(data, part=2))


