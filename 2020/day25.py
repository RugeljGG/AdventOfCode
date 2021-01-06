# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 05:58:28 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict, deque
import re

import aoc_helper
#
data = aoc_helper.get_input(25, force=True).strip()
# data = aoc_helper.get_input(25).strip()
print('Day 25 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

door, card = data.split()

door = int(door)
card = int(card)

v = 1
i = 0
c_i = None
d_i = None
while True:
    v = v * 7
    v %= 20201227
    if v == door:
        d_i = i
    if v == card:
        c_i = i
    if c_i is not None and d_i is not None:
        break

v = 1
for i in range(c_i):
    v = v * door
    v %= 20201227