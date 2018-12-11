# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 06:00:39 2018

@author: Gape
"""

import numpy as np


gridid = 9435
#gridid=18
size = 300

def get_powers(gridid, size):
    xs = np.repeat(np.arange(1,size+1)[np.newaxis, :], size, axis=0)
    ys = np.repeat(np.arange(1,size+1)[:, np.newaxis], size, axis=1)
    
    rack = (xs + 10)
    powers = rack * ys
    powers += gridid
    powers *= rack
    powers = (powers//100)%10
    powers -= 5

    return powers

def calculate(powers, size):
    i = size
    regions = sum(powers[:, j:300-i+1+j] for j in range(i))
    regions = sum(regions[j:300-i+1+j, :] for j in range(i))
    return regions
  

powers = get_powers(gridid, 300)
m = powers.max()
im = None

regions = calculate(powers, 3)
coords = np.unravel_index(regions.argmax(), regions.shape)
print('task 1:', coords[1]+1, coords[0]+1)


for i in range(2, 301):
    regions = calculate(powers, i)
    maximum = regions.max()
    if maximum > m:
        im = np.unravel_index(regions.argmax(), regions.shape), i
        m = maximum
        
coords, i = im
print('task 2:', coords[1]+1, coords[0]+1, i)