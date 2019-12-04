# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 05:56:11 2019

@author: gape
"""



with open('day3.txt') as file:
    data = []
    for row in file:
        data.append(row.strip().split(','))

def task1():    
    def move(d, x, y):
        if d == 'L':
            return x-1, y
        if d == 'U':
            return x, y+1
        if d == 'R':
            return x+1, y
        if d == 'D':
            return x, y-1
        
    w1 = set()
    x, y = 0, 0    
    for p in data[0]:
        for i in range(int(p[1:])):
            x, y = move(p[0], x, y)
    #        w1.append((x, y))
            w1.add((x,y))
    
    x, y = 0, 0
    closest = None
    for p in data[1]:
        for i in range(int(p[1:])):
            x, y = move(p[0], x, y)
    #        w2.append((x, y))
            if (x,y) in w1:
                if closest is None or (abs(x) + abs(y)) < closest:
                    closest = (abs(x) + abs(y))
                
    return closest

def task2():
    def move(d, x, y):
        if d == 'L':
            return x-1, y
        if d == 'U':
            return x, y+1
        if d == 'R':
            return x+1, y
        if d == 'D':
            return x, y-1
        
    w1 = dict()
    x, y = 0, 0
    l = 0
    for p in data[0]:
        for i in range(int(p[1:])):
            x, y = move(p[0], x, y)
            l+=1
    #        w1.append((x, y))
            w1[(x,y)] = l
    
    x, y = 0, 0
    l = 0
    closest = None
    for p in data[1]:
        for i in range(int(p[1:])):
            x, y = move(p[0], x, y)
            l+=1
    #        w2.append((x, y))
            if (x,y) in w1:
                if closest is None or w1[(x,y)] + l < closest:
                    closest = w1[(x,y)] + l
            
    return closest