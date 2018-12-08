# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 07:06:31 2018

@author: Gape
"""

from collections import defaultdict
from itertools import cycle

def task1():
    with open('day1.txt') as file:
        total = sum((int(row) for row in file))
    print('Task 1 result: ', total)
    
def task2(data=None):
    repeats = defaultdict(lambda: 0)
    total = 0
    if data is None:
        file = open('day1.txt')
        data = (int(row) for row in file)
            
    for i in cycle(data):
        repeats[total] +=1
        if repeats[total] >= 2:
            break
        total += i
    print('Task 2 result: ', total)
    file.close()