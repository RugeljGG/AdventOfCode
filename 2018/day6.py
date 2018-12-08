# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 05:58:15 2018

@author: Gape
"""
from collections import defaultdict, Counter

import numpy as np
import pandas as pd

with open('day6.txt') as file:
    coords = []
    for row in file:
        x, y = [int(c.strip()) for c in row.split(',')]
        coords.append([x,y])
        
    coords = np.array(coords)


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2 -y1)
def old(): # verjetno bi blo ok, sam je počasnej
    xmin, xmax = coords[:, 0].min(), coords[:, 0].max()
    ymin, ymax = coords[:, 1].min(), coords[:, 1].max()
    plane = np.ones(((xmax-xmin), (ymax-ymin)))*np.nan
    IDS = plane.copy()
    counts = Counter()
    for ID, (x0, y0) in enumerate(coords):
        print(ID)
        x = x0 - xmin
        y = y0 - ymin
        for i in range(plane.shape[0]):
            for j in range(plane.shape[1]):
                d0 = plane[i, j]
                d1 = distance((x,y), (i, j))
                if np.isnan(d0) or  d1 < d0:
                    plane[i, j] = d1
                    counts[IDS[i, j]] -= 1 
                    IDS[i, j] = ID
                    counts[ID] += 1
    
    for i in range(IDS.shape[0]):
        counts[IDS[i, 0]] = 0
        counts[IDS[i, -1]] = 0
    for j in range(IDS.shape[1]):
        counts[IDS[0, j]] = 0
        counts[IDS[-1, j]] = 0
 
    
def task1(coords):
    xmin, xmax = coords[:, 0].min(), coords[:, 0].max()+1
    ymin, ymax = coords[:, 1].min(), coords[:, 1].max()+1
    
    plane = np.ones(((xmax-xmin), (ymax-ymin)))*np.nan
    
    xs = np.repeat(np.arange(xmax-xmin)[:, np.newaxis], ymax-ymin, axis=1)
    ys = np.repeat(np.arange(ymax-ymin)[np.newaxis, :], xmax-xmin, axis=0)
    
    def d2(p1):
        x1, y1 = p1
        return abs(x1 - xs) + abs(y1 - ys)
    
    IDS = plane.copy()
    counts = defaultdict(lambda: 0)
    first = True
    for ID, (x0, y0) in enumerate(coords):
#        print(ID)
        x = x0 - xmin
        y = y0 - ymin
        d = d2((x,y))
        if first:
            plane = d
            IDS[:, :] = ID
            counts[ID] = plane.shape[0]*plane.shape[1]
            first = False
        else:
            better = d < plane
            same = d == plane
    #        plane[better] = d
            for i, j in list(zip(xs[better], ys[better])):
                plane[i, j] = d[i, j]
                counts[IDS[i, j]] -= 1
                IDS[i, j] = ID
                counts[IDS[i, j]] += 1
            for i, j in list(zip(xs[same], ys[same])):
                counts[IDS[i, j]] -= 1
                IDS[i, j] = -1
    
    for i in range(IDS.shape[0]):
        counts[IDS[i, 0]] = 0
        counts[IDS[i, -1]] = 0
    for j in range(IDS.shape[1]):
        counts[IDS[0, j]] = 0
        counts[IDS[-1, j]] = 0
        
    return pd.Series(counts).sort_values().iloc[-1]

def task2(coords, limit=10000):
    xmin, xmax = coords[:, 0].min(), coords[:, 0].max()+1
    ymin, ymax = coords[:, 1].min(), coords[:, 1].max()+1
    
    plane = np.zeros(((xmax-xmin), (ymax-ymin)))
    
    xs = np.repeat(np.arange(xmax-xmin)[:, np.newaxis], ymax-ymin, axis=1)
    ys = np.repeat(np.arange(ymax-ymin)[np.newaxis, :], xmax-xmin, axis=0)
    
    def d2(p1):
        x1, y1 = p1
        return abs(x1 - xs) + abs(y1 - ys)
    
    for ID, (x0, y0) in enumerate(coords):
#        print(ID)
        x = x0 - xmin
        y = y0 - ymin
        d = d2((x,y))
        plane += d

    return (plane<10000).sum()