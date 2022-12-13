# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 05:59:57 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper

data = aoc_helper.get_input(13, year=2022)
print('Day 13 input:')
print(data[:100])
print('Total input length: ', len(data))

# -1 = right, 1 = wrong, 0 = continue
def compare(p1, p2):
    for i in range(min((len(p1), len(p2)))):
        i1 = p1[i]
        i2 = p2[i]
        if isinstance(i1, int) and isinstance(i2, int):
            if i1 < i2:
                return -1
            elif i1 > i2:
                return 1
            else:
                continue
        else:
            if isinstance(i1, int):
                i1 = [i1]
            if isinstance(i2, int):
                i2 = [i2]
            a = compare(i1, i2)
            if a == 0:
                continue
            else:
                return a
    else:
        if len(p1) == len(p2):
            return 0
        elif len(p1) > len(p2):
            return 1
        else:
            return -1

i = 0
s = 0
for pair in data.strip().split('\n\n'):
    i+=1
    p1, p2 = (eval(p) for p in pair.split())
    c = compare(p1, p2)
    if c == -1:
        s += i

print("Task 1 answer:", s)

new = """[[2]]
[[6]]"""
packets = list((eval(p) for p in (data+new).strip().split() if p != '' ))
s = sorted(packets, key=cmp_to_key(compare))

a = 1
for i,p in enumerate(s):
    if p == [[2]] or p == [[6]]:
        a *= i+1

print("Task 2 answer:", a)