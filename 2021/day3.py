# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 05:58:29 2021

@author: gape
"""

from collections import Counter
import aoc_helper

data = aoc_helper.get_input(3, year=2021, force=True)

print('Day 3 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = data.split('\n')

nums = Counter()

for d in data:
    for i, b in enumerate(d):
        if b == '1':
            nums[i] += 1
            

gamma = []
epsi = []
for i in range(12):
    if nums[i] > 500:
        gamma += '1'
        epsi += '0'
    else:
        gamma += '0'
        epsi += '1'
        
print("Task 1: ", int(''.join(gamma), 2) *  int(''.join(epsi), 2))


oxy = data[:-1]
co2 = data[:-1]

for j in range(12):
    oxy_n = []
    nums = Counter()
    for d in oxy:
        for i, b in enumerate(d[j:]):
            if b == '1':
                nums[i+j] += 1
    for d in oxy:
        if (nums[j] >= len(oxy)/2 and d[j] == '1') or  (nums[j] < len(oxy)/2 and d[j] == '0'):
            oxy_n.append(d)
    oxy = oxy_n
    if len(oxy) <= 1:
        break

for j in range(12):
    co2_n = []
    
    nums = Counter()
    for d in co2:
        for i, b in enumerate(d[j:]):
            if b == '1':
                nums[i+j] += 1
                
    for d in co2:
        if (nums[j] >= len(co2)/2 and d[j] == '0') or  (nums[j] < len(co2)/2 and d[j] == '1'):
            co2_n.append(d)
    co2 = co2_n
    if len(co2) <= 1:
        break
    
print("Task 2: ", int(''.join(oxy), 2) *  int(''.join(co2), 2))