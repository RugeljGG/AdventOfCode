# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:54:54 2019

@author: gape
"""

def task1():
    with open('day1.txt') as file:
        total = 0
        for row in file:
            w = int(row)
            total += (w / 3) // 1 - 2
        
    print('Task 1 result: ', total)
    
def task2():
    with open('day1.txt') as file:
        total = 0
        for row in file:
            w = int(row)
            f = w
            while True:
                f1 = (f / 3) // 1 - 2
                if f1 >= 0:
                    f = f1
                    total += f1
                else:
                    break
        
    print('Task 2 result: ', total)