# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 05:58:10 2018

@author: Gape
"""

with open('day5.txt', 'r') as file:
    s = next(file).strip()
    
def task1(s):
    s = list(s)
    i = 0
    while i < len(s)-1:
        if s[i] != s[i+1] and s[i].upper() == s[i+1].upper():
            s.pop(i+1)
            s.pop(i)
            i -= 1
            if i < 0:
                i = 0
        else:
            i+=1
    return len(s)

def task2(s):
    removed = set()
    m = None
    b = ''
    for i in s:
        if i.upper() not in removed:
    #        print(i)
            r = task1(s.replace(i.upper(), '').replace(i.lower(),''))
            if m is None or r < m:
                b = i
                m = r
            removed.update(i.upper())
    return m, b