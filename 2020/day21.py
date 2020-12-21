# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 05:58:18 2020

@author: gape
"""


import copy
from collections import Counter, defaultdict
import re

import aoc_helper
#
data = aoc_helper.get_input(21, force=True).strip()
# data = aoc_helper.get_input(21).strip()
print('Day 21 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


candidates_alg = defaultdict(set)

all_ing = Counter()
for row in data.split('\n'):
    # print(row)
    ings, algs = row.split(' (')
    ings = ings.split(' ')
    ings = set(ings)
    algs = set(algs.strip(')').replace('contains ', '').split(', '))
    for ing in ings:
        all_ing[ing] += 1
    for alg in algs:
        if alg not in candidates_alg:
            candidates_alg[alg] = ings
        else:
            candidates_alg[alg] = ings.intersection(candidates_alg[alg])

possible = defaultdict(set)
for alg, ings in candidates_alg.items():
    for ing in ings:
        possible[ing].add(alg)

missing = set(all_ing.keys()) - set(possible.keys())
count = 0
for m in missing:
    count += all_ing[m]

print("Part 1 answer:" , count)

final = list()
while len(possible):
    for k in possible.keys():
        if len(possible[k]) == 1:
            v = list(possible.pop(k))[0]
            final.append((k,v))
            for k in possible.keys():
                try:
                    possible[k].remove(v)
                except KeyError:
                    pass
            break

print("Part 2 answer:" , ','.join(a[0] for a in sorted(final, key=lambda x: x[1])))