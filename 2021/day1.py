# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 05:47:17 2021

@author: gape
"""


import aoc_helper

data = aoc_helper.get_input(1, year=2021, force=True)

print('Day 1 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = [int(d) for d in data.split()]


def task1():
    p = 0
    s = 0
    for i in data:
        if i > p:
            s += 1
        p = i
    return s-1


def task2():
    s = 0
    ps = []
    for i in data:
        if len(ps)<3:
            ps.append(i)
            continue
        else:
            if sum(ps) < sum(ps[1:]) + i:
                s+=1
            ps = ps[1:] + [i]
    return s
        
print("Part 1 answer: ", task1())
print("Part 2 answer: ", task2())