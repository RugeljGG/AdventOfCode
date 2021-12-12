# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:12:04 2021

@author: gape
"""

from collections import Counter, defaultdict
import aoc_helper

data = aoc_helper.get_input(12, year=2021).strip()

print('Day 12 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

def find(start, used, m, l):
    if start == 'end':
        return 1
    s = 0
    used = used.copy()
    used.add(start)
    for p in points[start]:
        if p.islower() and p in used:
            if p in ('start', 'end'):
                continue
            elif m < l:
                s += find(p, used, m+1, l)
            else:
                continue
        else:
            s += find(p, used, m, l)
    return s


points = defaultdict(set)
for row in data.split('\n'):
    p1, p2 = row.split('-')
    points[p1].add(p2)
    points[p2].add(p1)
    

print("Part 1 answer:", find('start', set(), 0, 0))
print("Part 2 answer:", find('start', set(), 0, 1))