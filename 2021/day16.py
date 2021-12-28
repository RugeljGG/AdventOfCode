# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 06:23:35 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import prod
import re

import aoc_helper

data = aoc_helper.get_input(16, year=2021).strip()

print('Day 16 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


decoded = []
for c in data.strip():
    decoded.append('{:04b}'.format((int(c,16))))
    
decoded = ''.join(decoded)

def parse(s, start):
    version = int(s[start:start+3], 2)
    pt = int(s[start+3:start+6],2)
    value = None
    if pt == 4:
        data = []
        i = start+6
        while True:
            n = s[i:i+5]
            data.append((n[1:]))
            i+=5
            if n[0] == '0':
                break
        value = int(''.join(data), 2)
        end = i
    else:
        values = []
        lt = int(s[start+6],2)
        if lt == 0:
            length = int(s[start+7: start+22],2)
            sub = s[start+22:start+22+length]
            i = 0
            while i < length:
                new = parse(sub, i)
                i = new[3]
                version += new[0]
                values.append(new[2])
            end = i+start+22
        elif lt == 1:
            num = int(s[start+7: start+18],2)
            sub = s[start+18:]
            i = 0
            for j in range(num):
                new = parse(sub, i)
                i = new[3]
                version += new[0]
                values.append(new[2])
            end = i+start+18
        
        if pt == 0:
            value = sum(values)
        elif pt == 1:
            value = prod(values)
        elif pt == 2:
            value = min(values)
        elif pt == 3:
            value = max(values)
        elif pt == 5:
            value = values[0] > values[1]
        elif pt == 6:
            value = values[0] < values[1]
        elif pt == 7:
            value = values[0] == values[1]
            
    return version, pt, value, end
        
result = parse(decoded, 0)
print("Task 1 answer:", result[0])
print("Task 2 answer:", result[2])