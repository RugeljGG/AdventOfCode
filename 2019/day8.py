# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:34:44 2019

@author: gape
"""

with open('day8.txt') as file:
    data = next(file).strip()

#data = '0222112222120000'
        
def task1(w=25, h=6):
    n = w * h
    n_l = len(data) / n
    m = None
    for layer in range(int(n_l)):
        zs = 0
        os = 0
        ts = 0
        for char in range(n):
            if data[layer*n+char] == '0':
                zs+=1
            elif data[layer*n+char] == '1':
                os+=1
            elif data[layer*n+char] == '2':
                ts+=1
        if m is None or zs < m:
            m = zs
            result = os, ts
    
    return result[0]*result[1]


def task2(w=25, h=6):
    n = w*h
    n_l = len(data) / n
    picture = [['2' for i in range(w)] for j in range(h)]
    for layer in range(int(n_l)):
        for char in range(n):
            line = char % w
            row = char // w
            if picture[row][line] == '2':
                picture[row][line] = data[layer*n+char]
    
    for row in picture:
        print(''.join(row).replace('1', '#').replace('0', ' '))