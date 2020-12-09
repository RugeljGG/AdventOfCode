# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 05:54:09 2020

@author: gape
"""

from collections import defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(9, force=True).strip()
print('Day 9 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

data = [int(i) for i in data.split()]

for i in range(25, len(data)):
    correct = False
    for j in range(i-25, i-1):
        for k in range(j, i):
            if data[j] + data[k] == data[i]:
                # print(data[j],  data[k] , data[i])
                correct = True
                break
        if correct:
            break
    else:
        break

num = (data[i])
print("Part 1 answer: ", num)

for i in range(len(data)):
    s = data[i]
    j = i
    while s < num:
        j+=1
        s += data[j]
        if s == num:
            break
    else:
        continue
    break
    

print("Part 2 answer: ", min((data[i:j+1]))+max((data[i:j+1])))
