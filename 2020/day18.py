# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 05:57:42 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(18, force=True).strip()
# data = aoc_helper.get_input(18).strip()
print('Day 18 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


def calc_level_1(row):
    s = '+'
    total = 0
    level = 0
    i = 0
    while level >= 0 and i < len(row):
        
        c = row[i]
        if c == '(':
            new, new_i = calc_level_1(row[i+1:])
            if s == '+':
                total += int(new)
            elif s == '*':
                total *= int(new)
            i += new_i + 1
        elif c == ')':
            level -=1 
            break
        elif c in ('+', '*'):
            s = c
        elif c == ' ':
            pass
        else:
            if s == '+':
                total += int(c)
            elif s == '*':
                total *= int(c)
        i+=1
    
    return total, i


def calc_level_2(row, r='('):
    s = '+'
    total = 0
    level = 0
    i = 0
    while level >= 0 and i < len(row):
        
        c = row[i]
        if c == '(':
            new, new_i = calc_level_2(row[i+1:])
            if s == '+':
                total += int(new)
            elif s == '*':
                total *= int(new)
            i += new_i + 1
        elif c == ')':
            level -=1 
            if r == '*':
                i-= 1
            break
        elif c == '*':
            if r == '*':
                i-= 1
                break
            else:
                s = '*'
                new, new_i = calc_level_2(row[i+1:], '*')
                total *= int(new)
                i += new_i + 1
        elif c == '+':
            s = c
        elif c == ' ':
            pass
        else:
            if s == '+':
                total += int(c)
            elif s == '*':
                total *= int(c)
        i+=1

    return total, i
            
total = 0
for row in data.split('\n'):
    total += calc_level_1(row)[0]
    
print(total)

print("Part 1 answer:", total)

total = 0
for row in data.split('\n'):
    total += calc_level_2(row)[0]
    
print("Part 2 answer:", total)