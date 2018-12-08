# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 05:56:10 2018

@author: Gape
"""

from collections import defaultdict
from itertools import cycle

def task1():
    with open('day2.txt') as file:
        tw = 0
        tr = 0
        for row in file:
            counts = defaultdict(lambda: 0)
            for letter in row:
                counts[letter] += 1
            if 2 in counts.values():
                tw +=1
            if 3 in counts.values():
                tr +=1
        print(tw*tr)
    
def task2():
    with open('day2.txt') as file:
        boxes = [row.strip() for row in file]
        
        for i, b1 in enumerate(boxes):
            for b2 in boxes[i+1:]:
                diff = 0
                for j in range(len(b1)):
                    if b1[j] != b2[j]:
                        diff += 1
                if diff == 1:
                    code = ''
                    for j in range(len(b1)):
                        if b1[j] == b2[j]:
                            code += b1[j]
                    print(b1, b2, code)