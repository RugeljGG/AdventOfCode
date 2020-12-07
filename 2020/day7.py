# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 05:57:35 2020

@author: gape
"""

from collections import defaultdict
import re

import aoc_helper
data = aoc_helper.get_input(7, force=True).strip()
# data = aoc_helper.get_input(7).strip()

print('Day 7 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

bags = dict()

class Bag():
    def __init__(self, name):
        self.upper = []
        self.lower = []
        self.name = name
        self.l_num = None
        
    def find_upper(self, counted=set()):
        for u in self.upper:
            if u.name in counted:
                continue
            else:
                counted.add(u.name)
                u.find_upper(counted)
        return len(counted)
        
    def find_lower(self):
        num = 0
        if self.l_num is None:
            for count, u in self.lower:
                num += count
                num += count * u.find_lower()
            self.l_num = num
            return num
        else:
            return self.l_num



for row in data.split('\n'):
    k, v = row.split(' bags contain ')
    if k in bags:
        hbag = bags[k]
    else:
        hbag = Bag(k)
        bags[k] = hbag
    if v == 'no other bags.':
        continue
    else:
        children = v.split(', ')
        for ch in children:
            num, c1, c2, _ = ch.split(' ')
            name =  ' '.join((c1, c2))
            if name in bags:
                lbag = bags[name]
            else:
                lbag = Bag(name)
                bags[name] = lbag
                
            hbag.lower.append((int(num), lbag))
            lbag.upper.append(hbag)

print("Part 1 answer: ", bags['shiny gold'].find_upper())
print("Part 2 answer: ", bags['shiny gold'].find_lower())