# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 06:18:21 2019

@author: gape
"""

from collections import defaultdict
import math

roids = []
with open('day10.txt') as file:
    for y, row in enumerate(file):
        for x, c in enumerate(row.strip()):
            if c == '#':
                roids.append((x,y))
    
m = 0
b = None
for x0, y0 in roids:
    angles = defaultdict(lambda: list())
    for x1, y1 in roids:
        if x0 == x1 and y0 == y1:
            continue
        angles[math.atan2(x1-x0, (y1-y0))].append([x1, y1])
    if len(angles) > m:
        m = len(angles)
        b = x0, y0
        b_a = angles

print("task 1: ", m)

x0, y0 = b
s_a = dict()
for angle, targets in b_a.items():
    s_a[angle] = sorted(targets, key=lambda x: (x[0]-x0)**2 + (x[1]-y0)**2, reverse=True)
    
i = 0
for angle, targets in sorted(s_a.items(), key=lambda x: x[0], reverse=True):
    x, y = targets.pop()
    i += 1
#    print(x,y)
    if i == 200:
        break
    
print("task 2: ", x*100+y)