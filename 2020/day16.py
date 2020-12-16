# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 05:58:48 2020

@author: gape
"""

from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(16, force=True).strip()
# data = aoc_helper.get_input(16).strip()
print('Day 16 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

rules = dict()

r, your, other = data.split('\n\n')

rate = 0
for row in r.split('\n'):
    rule, value = row.split(': ')
    v1, v2 = value.split(' or ')
    v1s, v1e = v1.split('-')
    v2s, v2e = v2.split('-')
    rules[rule] = [(int(v1s), int(v1e)), (int(v2s), int(v2e))]
    
valid_t = []
for ticket in other.split('\n')[1:]:
    values = [int(c) for c in ticket.split(',')]
    valid = True
    for v in values: 
        for rv in rules.values():
            (v1s, v1e) = rv[0]
            (v2s, v2e) = rv[1]
            if (v >= v1s and v <= v1e) or (v >= v2s and v <= v2e):
                break
        else:
            rate += v
            valid = False
    if valid:
        valid_t.append(values)
        
print("Part 1 answer:", rate)


possible = defaultdict(set)
impossible = defaultdict(set)
for ticket in valid_t:
    for i, v in enumerate(ticket):
        for rn, rv in rules.items():
            (v1s, v1e) = rv[0]
            (v2s, v2e) = rv[1]
            if (v >= v1s and v <= v1e) or (v >= v2s and v <= v2e):
                possible[rn].add(i)
            else:
                impossible[rn].add(i)
                
for rn, values in impossible.items():
    possible[rn] -= values
        
taken = set()
correct = dict()

while len(taken) < 20:
    for rn, values in possible.items():
        if not len(values) :
            continue
        # print(len(values))
        for t in taken:
            try:
                possible[rn].remove(t)
            except KeyError:
                pass
        if len(values) == 1:
            cv = values.pop()
            correct[rn] = cv
            taken.add(cv)
            
your_values = [int(c) for c in your.split('\n')[1].split(',')]
total = 1
for kn, v in correct.items():
    if 'departure' in kn:
        total *= your_values[v]
        
print("Part 2 answer:", total)