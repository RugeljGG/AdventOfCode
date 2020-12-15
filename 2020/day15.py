# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:59:14 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(15, force=True).strip()
# data = aoc_helper.get_input(15).strip()
print('Day 15input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


def solve(data, target):
    spoken = Counter()
    for i, n in enumerate(data.split(',')):
        spoken[int(n)] = i
    
    n = 0
    while i<target-1:
        # if i % 5000000 == 0:
        #     print(i, flush=True)
        i+=1
        last = n
        if n in spoken:
            n = i-spoken[n]
        else:
            n = 0
        spoken[last] = i
    return last
    
print("Part 1 answer: ", solve(data, 2020))
print("Solving part 2 Brute force... ", end='')
print("Part 2 answer: ", solve(data, 30000000))