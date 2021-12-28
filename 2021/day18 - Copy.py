# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 08:09:25 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(18, year=2021).strip()

print('Day 18 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

class SFN:
    def __init__(self, num, level):
        self.level = level
        self.num = num
        self.left = None
        self.right = None
        
    def check_explode(self):
        if self.level > 4:
            new = SFN(0, self.level)
            new.left = self.left
            new.right = self.right.right
            if self.left is not None:
                self.left.num += self.num
                self.left.right = new
            if self.right.right is not None:
                self.right.right.num += self.right.num
                self.right.right.left = new
                return self.right.right.check_explode() + 1
            else:
                return 1
        elif self.right is not None:
            return self.right.check_explode()
        else:
            return 0
            
    def check_split(self):
        if self.num >= 10:
            l = SFN(floor(self.num/2), self.level+1)
            r = SFN(ceil(self.num/2), self.level+1)
            if self.left is not None:
                self.left.right = l
                l.left = self.left
            l.right = r
            r.left = l
            if self.right is not None:
                self.right.left = r
                r.right = self.right
            return l
        elif self.right is not None:
            return self.right.check_split()
        else:
            return 0
            
                
    

# rows = deque()
# for row in data.split('\n'):
#     numbers = []
#     left = None
#     l = 0
#     data = []
#     cur = data
#     for c in row:
#         if c == '[':
#             l += 1
#             cur.append([])
#             cur
#         elif c == ']':
#             l -= 1
#         elif c.isdigit():
#             num = SFN(int(c), l)
#             num.left = left
#             if left is not None:
#                 left.right = num
#             numbers.append(num)
#             left = num
#         elif c == ',':
#             continue
#         else:
#             print("error:", c)
#     rows.append(numbers)

rows = deque()
for row in data.split('\n'):
    numbers = []
    left = None
    l = 0
    data = []
    cur = data
    for c in row:
        data = eval(row)
    rows.append(numbers)
start = SFN(-100, -100)    
start.right = numbers[0]
numbers[0].left = start

