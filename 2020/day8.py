# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:43:17 2020

@author: gape
"""

from collections import defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(8, force=True).strip()

print('Day 8 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


data = data.strip().split('\n')
i = 0
acc = 0

visited = set()
while i < len(data):
    t, num = data[i].split(' ')
    num = int(num)
    
    if i in visited:
        break
    
    else:
        visited.add(i)
        if t == 'nop':
            i+=1
            continue
        if t == 'acc':
            i+=1
            acc += num
        if t == 'jmp':
            i += num
        
print("Part 1 answer: ", acc)
    


visited = set()
cache = visited, 0, 0
tested = set()

finished = False
while not finished:
    visited = cache[0]
    i = cache[1]
    acc = cache[2]
    
    while i < len(data):
        t, num = data[i].split(' ')
        num = int(num)
        visited.add(i)
        if t == 'acc':
            i+=1
            acc += num
            continue

        
        if i not in tested:
            tested.add(i)
            cache = visited.copy(), i, acc
            if t == 'nop':
                i += num    
            if t == 'jmp':
                i+=1
        else:
            if t == 'nop':
                i+=1
                continue
            if t == 'jmp':
                i += num
                continue

        while i < len(data):
            t, num = data[i].split(' ')
            num = int(num)
            
            if i in visited:
                break
            
            else:
                visited.add(i)
                if t == 'nop':
                    i+=1
                    continue
                if t == 'acc':
                    i+=1
                    acc += num
                if t == 'jmp':
                    i += num
        else:
            finished = True
        
        break
    
print("Part 2 answer: ", acc)
    