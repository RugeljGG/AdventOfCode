# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:57:17 2022

@author: gape
"""

from collections import Counter
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(1, year=2023)
print('Day 1 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [d for d in data.strip().split('\n')]
# data = [int(d) for d in data.strip().split('\n')]

l = []
for i in data:
    nums = re.findall('\d', i)
    l.append(int(nums[0])*10 + int(nums[-1]))

print("Task 1 answer:", sum(l))


mapping = {'one':1,
        'two':2,
        'three':3,
        'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

l2 = []
for i in data:
    nums = re.findall('\d'+'|'+'|'.join(mapping.keys()), i)
    if len(nums[0]) == 1:
        first = int(nums[0])
    else:
        first = mapping[nums[0]]

    if len(nums[-1]) == 1:
        last = int(nums[-1])
    else:
        last = mapping[nums[-1]]

    l2.append(first*10+last)


print("Task 2 answer:", sum(l2))