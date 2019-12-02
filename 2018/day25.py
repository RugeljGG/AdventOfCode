# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 12:47:08 2018

@author: Gape
"""

from collections import defaultdict

import scipy as sp

points = []
with open('day25.txt') as file:
    for row in file:
        points.append(tuple(int(i) for i in row.split(',')))

dist = sp.spatial.distance.pdist(points, metric='cityblock') 
dist = sp.spatial.distance.squareform(dist)

pairs = defaultdict(set)
for p1, p2 in sp.argwhere(dist <= 3):
    if p1 != p2:
        pairs[p1].add(p2)
    
for p in range(len(points)):
    values = pairs[p]
    joined = False
    for v in values:
        if v > p:
            pairs[v].update(values)
            joined = True
    if joined:
        pairs.pop(p)
        
print(len(pairs))