# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 06:01:15 2018

@author: Gape
"""

import re

import numpy as np
import scipy as sp
import scipy.spatial
 
data = []
with open('day23.txt') as file:
    for row in file:
        res = re.findall('pos=<(\-?\d*),(\-?\d*),(\-?\d*)>, r=(\-?\d*)', row.strip())
        x, y, z, r = [int(c) for c in res[0]]
        data.append((x, y, z, r))
        

points = np.array([p[:3] for p in data])
ranges = np.array([p[3] for p in data])

def distance(p1, p2):
    return sum(abs(p1[i]-p2[i]) for i in range(3))


def zone_check(lims, i, data, minimal=0):
    delta = 1e7 / (10**i)
    
    mx, mix, my, miy, mz, miz = lims
    xs = np.arange(int(mix/delta), int(mx/delta))
    ys = np.arange(int(miy/delta), int(my/delta))
    zs = np.arange(int(miz/delta), int(mz/delta))
    
    # https://stackoverflow.com/questions/1208118/using-numpy-to-build-an-array-of-all-combinations-of-two-arrays/1235363
    zone = np.array(np.meshgrid(xs, ys, zs)).T.reshape(-1, 3)
    margin = 3 if i < 7 else 0
    
#    values = np.zeros(zone.shape[0])
#    for bot in data:
#        p = np.array(bot[:3])/delta
#        limit = bot[3]/delta+margin
#        values[sp.spatial.distance.cdist(zone, [p], metric='cityblock')[:, 0]<=limit] += 1

#    points = np.array([p[:3] for p in data]) / delta
#    ranges = np.array([p[3] for p in data]) / delta + margin
    values = (sp.spatial.distance.cdist(zone, points/delta, metric='cityblock') <= ranges/delta+margin).sum(axis=1)

    rank = np.argsort(values)[::-1]
    zone = zone[rank]
    values = values[rank]
#    print(i, len(zone), flush=True)
    best = (None, minimal)
    if i == 7:
        return zone[0], values[0]
    for p, value in zip(zone, values):      
        p = p * delta
        if value < best[1]:
            break
        lims = (p[0]+delta, p[0]-delta, 
                p[1]+delta, p[1]-delta, 
                p[2]+delta, p[2]-delta)
        b = zone_check(lims,i+1, data, minimal=best[1]+1)
#        print(i, b, value)
        if b[0] is not None and b[1] >= best[1]:
#            print(i, b, flush=True)
            best = b
    return best


def task1():
    inrange = []

    for bot1 in data:
        inrange.append(0)
        for bot2 in data:
            if distance(bot1[:3], bot2[:3]) <= bot1[3]:
                inrange[-1]+=1 
        
    return (inrange[data.index(max(data, key=lambda x: x[3]))])

def task2():
    mx = None
    mix = None
    my = None
    miy = None
    mz = None
    miz = None
    
    for bot in data:
        if mx is None or bot[0] > mx:
            mx = bot[0] 
        if mix is None or bot[0] < mix:
            mix = bot[0] 
        if my is None or bot[1] > my:
            my = bot[1] 
        if miy is None or bot[1] < miy:
            miy = bot[1]
        if mz is None or bot[2] > mz:
            mz = bot[2] 
        if miz is None or bot[2] < miz:
            miz = bot[2]
            
    
    lims = mx, mix, my, miy, mz, miz
    best = zone_check(lims, 0, data, minimal = 900)
    return sum(best[0])
