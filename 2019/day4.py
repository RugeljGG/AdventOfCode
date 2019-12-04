# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 05:58:02 2019

@author: gape
"""

s1 = 245318
s2 = 765747

def task1():
    count = 0
    for i in range(s1, s2+1):
        n = str(i)
        double = False
        for j in range(1, 6):
            if n[j] == n[j-1]:
                double = j
            if n[j] < n[j-1]:
                break
        else:
            if double:
                count += 1
    return count

def task2():
    count = 0    
    for i in range(s1, s2+1):
        n = str(i)
        double = 0
        doublef = False
        for j in range(1, 6):
            if n[j] == n[j-1]:
                double += 1
            else:
                if double == 1:
                    doublef = True
                double = 0
            if n[j] < n[j-1]:
                break
        else:
            if double == 1:
                doublef = True
            if doublef:
                count += 1
    return count