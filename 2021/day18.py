# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:27:25 2021

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
    def __init__(self, data, level, isleft, parent):
        left, right = data
        if isinstance(left, int):
            self.left = left
        elif isinstance(left, SFN):
            self.left = left
            self.left.isleft = True
            self.left.parent = self
        else:
            self.left = SFN(left, level+1, True, self)
        
        if isinstance(right, int):
            self.right = right
        elif isinstance(right, SFN):
            self.right = right
            self.right.isleft = False
            self.right.parent = self
        else:
            self.right = SFN(right, level+1, False, self)
            
        self.level = level
        self.isleft = isleft
        self.parent = parent
        
        
    def raise_level(self):
        self.level +=1
        if self.level >= 4:
            # print(self, '\t\t', self.show())
            self.parent.raise_left(self.left, self.isleft)
            self.parent.raise_right(self.right, self.isleft)
            if self.isleft:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return 1
        else:
            n = 0
            if isinstance(self.left, SFN):
                n += self.left.raise_level()
            if isinstance(self.right, SFN):
                n += self.right.raise_level()
            return n
           
    
    def raise_left(self, num, isleft):
        if isleft:
            if self.parent:
                self.parent.raise_left(num, self.isleft)
        else:
            if isinstance(self.left, int):
                # print(self, num, "left1")
                self.left += num
            else:
                target = self.left
                while not isinstance(target.right, int):
                    target = target.right
                # print(self, num, "left2")
                target.right += num
    
    def raise_right(self, num, isleft):
        if not isleft:
            if self.parent:
                self.parent.raise_right(num, self.isleft)
        else:
            if isinstance(self.right, int):
                # print(self, num, "right1")
                self.right += num
            else:
                target = self.right
                while not isinstance(target.left, int):
                    target = target.left
                # print(self, num, "right2")
                target.left += num
    
    
    def check_split(self):
        n = 0
        if isinstance(self.left, int):
            if self.left >= 10:
                # print(self.left, '\t\t\t', self.show())
                l = floor(self.left/2)
                r = ceil(self.left/2)
                self.left = SFN([l,r], self.level, True, self)
                if self.left.raise_level():
                    return -1
                n += 1
                

        if not isinstance(self.left, int):
            num = self.left.check_split()
            if num == -1:
                return -1
            n += num
            
        if isinstance(self.right, int):
            if self.right >= 10:
                # print(self.right, '\t\t\t', self.show())
                l = floor(self.right/2)
                r = ceil(self.right/2)
                self.right = SFN([l,r], self.level, False, self)
                if self.right.raise_level():
                    return -1
                n += 1
                
        if not isinstance(self.right, int):
            num = self.right.check_split()
            if num == -1:
                return -1
            n += num
        return n
            
    
    def calc(self):
        if isinstance(self.left, SFN):
            l = self.left.calc()
        else:
            l = self.left
        
        if isinstance(self.right, SFN):
            r = self.right.calc()
        else:
            r = self.right
        
        return 3*l + 2*r
        
    def show(self):
        if self.parent:
            return self.parent.show()
        else:
            return self
            
    def __repr__(self):
        return "[{},{}]".format(self.left, self.right)
        

rows = list()
for row in data.split('\n'):
    rows.append(eval(row))
    # rows.append(SFN(data, 0, False, None))

head = SFN(rows[0], 0, False, None)
for i in range(1, len(rows)):
    a = head
    # print(' ', a)
    b = SFN(rows[i], 0, False, None)
    # print('+', b)
    head = SFN([a, b], -1, True, None)
    head.raise_level()
    while True:
        r = head.check_split()
        if r == 0:
            break
    # print('=', head)
    # print()
    
print("Part 1 answer:", head.calc())

best = 0
for i in range(len(rows)):
    for j in range(len(rows)):
        if i == j:
            continue
        a = SFN(rows[i], 0, False, None)
        b = SFN(rows[j], 0, False, None)
        head = SFN([a, b], -1, True, None)
        head.raise_level()
        while True:
            r = head.check_split()
            if r == 0:
                break
        calc = head.calc()
        if calc > best:
            best = calc
            

print("Part 2 answer:", best)