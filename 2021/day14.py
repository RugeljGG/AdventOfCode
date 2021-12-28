# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:35:28 2021

@author: gape
"""

from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(14, year=2021).strip()

print('Day 14 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = data.split('\n')

start = data[0]

ins = dict()
for row in data[2:]:
    s, e = row.split(' -> ')
    ins[s] = e

mapper = defaultdict(list)
cnt = Counter()

for s, e in ins.items():
    if s[0]+e in ins:
        mapper[s].append(s[0]+e)
    if e+s[1] in ins:
        mapper[s].append(e+s[1])

full = start
result = Counter()  
for i in range(len(full)-1):
    c1 = full[i]
    c2 = full[i+1]
    if c1+c2 in ins:
        cnt[c1+c2] += 1
    result[c1] += 1
result[c2] += 1

for step in range(40):
    cnt_new = cnt.copy()
    for s, c in cnt.items():
        if c > 0:
            result[ins[s]] += c
            for e in mapper[s]:
                cnt_new[e]+=c
            cnt_new[s] -= c
    cnt = cnt_new
    
    if step == 9:
        print("Part 1 answer:", max(result.values()) - min(result.values()))
    if step == 39:
        print("Part 2 answer:", max(result.values()) - min(result.values()))
        
    