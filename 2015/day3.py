# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:04:31 2020

@author: gape
"""

from collections import defaultdict
import re

import aoc_helper
data = aoc_helper.get_input(3, year=2015, force=True).strip()

print('Day 3 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


x, y = 0, 0

moves = dict('^' = (0, 1),
             '<' = (-1, 0),
             '>' = (đ
for c in data:
    