# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 05:58:52 2022

@author: gape
"""

from collections import Counter
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(4, year=2022)
print('Day 4 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]

s = 0
s2 = 0
for row in data:
    e1, e2 = row.split(',')
    e1 = e1.split('-')
    e2 = e2.split('-')

    if int(e1[0]) <= int(e2[0]) and int(e1[1]) >= int(e2[1]):
        s+=1
    elif int(e1[0]) >= int(e2[0]) and int(e1[1]) <= int(e2[1]):
        s+=1


    if int(e1[0]) <= int(e2[1]) and int(e1[1]) >= int(e2[0]):
        s2+=1


print("Task 1 answer:", s)
print("Task 2 answer:", s2)