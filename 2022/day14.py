# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 05:57:54 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper

data = aoc_helper.get_input(14, year=2022)
print('Day 14 input:')
print(data[:100])
print('Total input length: ', len(data))


def show(blocked):
    minx = min(blocked, key=lambda x: x[0])[0]
    maxx = max(blocked, key=lambda x: x[0])[0]
    miny = min(blocked, key=lambda x: x[1])[1]
    maxy = max(blocked, key=lambda x: x[1])[1]
    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            c = blocked.get((x, y), ' ')
            print(c, end='')
        print()

# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

def solve(part=1):

    blocked = dict()

    maxy = 0
    maxx = 0
    minx = 500


    for row in data.strip().split('\n'):
        paths = [[int(x) for x in p.split(',')] for p in row.split(' -> ')]
        start = paths[0]
        for end in paths[1:]:

            for x in range(min((start[0], end[0])), max((start[0],end[0]))+1):
                for y in range(min((start[1], end[1])), max((start[1],end[1]))+1):
                    blocked[(x,y)] = '#'
                    if y > maxy:
                        maxy = y
                    if x > maxx:
                        maxx = x
                    if x < minx:
                        minx = x
            start = end

    maxy = maxy+1

    s = 0
    while True:
        x, y = 500, 0
        while True:
            if (x, y+1) not in blocked and y<maxy:
                y += 1
            elif (x-1, y+1) not in blocked and y<maxy:
                x -= 1
                y += 1
            elif (x+1, y+1) not in blocked and y<maxy:
                x += 1
                y += 1
            else:
                blocked[(x,y)] = 'O'
                s += 1
                break
            if y > maxy:
                print('ne sme')
                break

        if part==1 and y == maxy:
            return s-1
        elif part ==2 and (x,y ) == (500,0):
            return s


print("Task 1 answer:", solve(part=1))
print("Task 2 answer:", solve(part=2))
