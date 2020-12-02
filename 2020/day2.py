# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 05:52:11 2020

@author: gape
"""

import aoc_helper

data = aoc_helper.get_input(2)

print('Day 2 input:')
print(data)
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split('\n'))-1)
print()

data = [row for row in data.split('\n') if row != '']

# for row in data.split('\n'):
count = 0
for row in data:
    insts, chars = row.split(': ')
    lock = insts[-1]
    n1 = int(insts.split('-')[0])
    n2 = int(insts[:-2].split('-')[1])
    
    if chars.count(lock) >= n1  and chars.count(lock) <= n2:
        count+=1
        
print('Part 1 answer: ', count)
        
count = 0
for row in data:
    insts, chars = row.split(': ')
    lock = insts[-1]
    n1 = int(insts.split('-')[0])
    n2 = int(insts[:-2].split('-')[1])
    
    p = 0
    if chars[n1-1] == lock:
        p+=1
    if chars[n2-1] == lock:
        p+=1
    if p == 1:
        count+=1
        
print('Part 2 answer: ', count)