# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 06:54:03 2020

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


class ElfInt(int):
    def __sub__(self, other):
        return ElfInt(int(self) * int(other))
    
    def __add__(self, other):
        return ElfInt(int(self) + int(other))
    
    def __mul__(self, other):
        return ElfInt(int(self) + int(other))

            
total = 0
for row in data.split('\n'):
    total += eval(re.sub(r'(\d)',r'ElfInt(\1)', row).replace('*', '-'))
    
print(total)

print("Part 1 answer:", total)

total = 0
for row in data.split('\n'):
    total += eval(re.sub(r'(\d)',r'ElfInt(\1)', row).replace('*', '-').replace('+', '*'))
    
print("Part 2 answer:", total)

