# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 05:57:25 2018

@author: Gape
"""

from collections import defaultdict
from itertools import cycle

import numpy as np

def task1():
    with open('day3.txt') as file:
        fabric = np.zeros((1000, 1000))
        for row in file:
            first, rest = row.split('@')
            position, size = rest.split(':')
            x, y = (int(p.strip()) for p in position.split(','))
            h, w = (int(s.strip()) for s in size.split('x'))
            
            for i in range(h):
                for j in range(w):
                    fabric[x+i, y+j] += 1
        
        print(np.unique(fabric, return_counts=True)[1][2:].sum())
    
#def task2():
with open('day3.txt') as file:
    fabric = np.zeros((1000, 1000))
    claims = dict()
    for row in file:
        first, rest = row.split('@')
        ID = int(first.replace('#', '').strip())
        position, size = rest.split(':')
        x, y = (int(p.strip()) for p in position.split(','))
        h, w = (int(s.strip()) for s in size.split('x'))
        
    
    
        overlap = False
        for i in range(h):
            for j in range(w):
                if fabric[x+i, y+j] != 0:
                    claims[fabric[x+i, y+j]] = False
                    overlap = True
                fabric[x+i, y+j] = ID
        if not overlap:
            claims[ID] = True
                

    for i, v in claims.items():
        if v:
            print(i)