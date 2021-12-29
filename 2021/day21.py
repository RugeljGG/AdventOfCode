# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:56:33 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(21, year=2021).strip()

print('Day 21 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

pos = [int(i) for i in re.findall('starting position: (\d)', data)]
# pos = [4, 8]


def task1(pos):
    s = [0, 0]
    num = 0
    dice = 0
    rolls = 0
    while s[0] < 1000 and s[1] < 1000:
        i = num % 2
        roll = 0
        for j in range(3):
            rolls += 1
            dice = dice % 100 + 1
            roll += dice
        pos[i] = (pos[i]+roll-1) % 10 + 1
        s[i] += pos[i]
        num += 1
    
    return (min(s) * rolls)


def task2(pos):
    def throw(score, pos, level, countwin, countlose, multi):
        for roll, c in rolls.items():
            p_n = (pos+roll-1)%10+1
            if score+p_n >= 21:
                countwin[level] += multi * c
            else:
                countlose[level] += multi * c
                throw(score+p_n, p_n, level+1, countwin, countlose, multi*c)
    
    rolls = Counter()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r = sum((i+1,j+1,k+1))
                rolls[r]+=1
    
    p1countwin = Counter()
    p2countwin = Counter()
    p1countlose = Counter()
    p2countlose = Counter()
    
        
    throw(0, pos[0], 1, p1countwin, p1countlose, 1)
    throw(0, pos[1], 1, p2countwin, p2countlose, 1)
    
    p1wins = 0
    p2wins = 0
    
    for p1, v1 in p1countwin.items():
        p1wins += v1 * p2countlose[p1-1]
        
    for p2, v2 in p2countwin.items():
        p2wins += v2 * p1countlose[p2]
        
    return max(p1wins, p2wins)
    
print("Task 1 answer:", task1(pos.copy()))
print("Task 2 answer:", task2(pos.copy()))