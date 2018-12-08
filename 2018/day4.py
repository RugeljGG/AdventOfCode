# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 05:54:03 2018

@author: Gape
"""

from collections import defaultdict
from itertools import cycle
import re

import numpy as np
import pandas as pd

with open('day4.txt') as file:
    entries = dict()
    for row in file:
        res =  re.search('\[(.*)\] (.*)', row)
        ts = res[1]
        ts = '2018' + ts[4:]
        entries[ts] = res[2]
    
    entries = pd.Series(entries)
    entries.index = pd.to_datetime(entries.index)
    entries = entries.sort_index()
    
    guards = []
    for ts, ent in entries.items():
        res = re.search('#(\d*)',ent)
        if res is not None:
            guards.append([int(res[1])])
        else:
            guards[-1].append(ts.minute)
            
    guards =pd.DataFrame(guards)
    guards = guards.set_index(0)
    results = dict()
    for guard, rows in guards.groupby(level=0):
        asleep = np.zeros(60)
        for data in rows.values:
            for i in range(int(len(data)/2)):
                if not pd.isnull(data[i*2]):
                    asleep[int(data[i*2]):int(data[i*2+1])] += 1
        results[guard] = sum(asleep), asleep
    maximum_l =[0,0,None]
    maximum_t =[0,0,None]
    for g, d in results.items():
        if d[0]>maximum_l[1]:
            maximum_l = [g, d[0], d[1]]
        t = d[1].max()
        if t>maximum_t[1]:
            maximum_t = [g, t, d[1]]
    print ('part 1 result:', maximum_l[2].argmax() * maximum_l[0])
    print ('part 2 result:', maximum_t[2].argmax() * maximum_t[0])