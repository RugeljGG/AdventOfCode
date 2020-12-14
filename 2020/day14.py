# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 05:56:35 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(14, force=True).strip()
# data = aoc_helper.get_input(14).strip()
print('Day 14 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

memory=Counter()
for row in data.split('\n'):
    k, v = row.split(' = ')
    if k == 'mask':
        mask = v
    else:
        i = re.findall('\[(\d.*?)\]', k)[0]
        value = [c for c in '{0:036b}'.format(int(v))]
        
        for j in range(len(value)):
            if mask[-j-1] == 'X':
                continue
            else:
                value[-j-1] = mask[-j-1]
        memory[i] = int(''.join(value), base=2)
 
    
print("Part 1 answer: ", sum(memory.values()))
    

def locator(i, s):
    if i == len(s):
        return [s]
    else:
        if s[i] == 'X':
            pre = s[:i]
            post = s[i+1:]
            return locator(i+1, pre+'1'+post) +  locator(i+1, pre+'0'+post)
        else:
            return locator(i+1, s)

memory=dict()
for row in data.split('\n'):
    k, v = row.split(' = ')
    if k == 'mask':
        mask = v
    else:
        i = re.findall('\[(\d.*?)\]', k)[0]
        position = [c for c in '{0:036b}'.format(int(i))]
        
        for j in range(len(position)):
            if mask[-j-1] == '0':
                continue
            else:
                position[-j-1] = mask[-j-1]
        for position in locator(0, ''.join(position)):
            memory[int(position, base=2)] = int(v)

        
print("Part 2 answer: ", sum(memory.values()))