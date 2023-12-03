# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:43:59 2020

@author: gape
"""

import aoc_helper
data = aoc_helper.get_input(2, year=2015, force=True).strip()

presents = []
count = 0
count2 = 0
for row in data.split():
    l, w, h = [int(i) for i in row.split('x')]
    presents.append([l, w, h])
    p1, p2, p3 =  2*l*w, 2*w*h, 2*h*l
    count += p1 + p2 + p3 + min((p1, p2, p3))/2
    count2 += sum(sorted([l,w,h])[:2])*2 + l*w*h
    
print(count)
