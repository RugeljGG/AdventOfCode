# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:58:44 2023

@author: gape
"""

from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(15, year=2023)
print('Day 15 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
data = [d for d in data.strip().split(',')]

def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v


print("Task 1 answer:", sum((h(s) for s in data)))

boxes = defaultdict(list)
boxes_v = defaultdict(dict)

for s in data:
    if '-' in s:
        label, l = s.split('-')
        num = h(label)
        if label in boxes_v[num]:
            boxes[num].remove(label)
            boxes_v[num].pop(label)

    elif '=' in s:
        label, l = s.split('=')
        num = h(label)
        if label not in boxes_v[num]:

            boxes[num].append(label)
        boxes_v[num][label] = int(l)


    else:
        print("ojoj")

value = 0
for k, box in boxes.items():
    for i, label in enumerate(box):
        value += (k+1) * (i+1) * boxes_v[k][label]

print("Task 2 answer:", value)