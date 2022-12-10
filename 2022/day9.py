# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 05:58:12 2022

@author: gape
"""


from collections import Counter, defaultdict, deque
import numpy as np
import re

import aoc_helper

data = aoc_helper.get_input(9, year=2022)
print('Day 9 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

def move(pos, d):
    if d == 'U':
        return pos[0]-1, pos[1]
    if d == 'D':
        return pos[0]+1, pos[1]
    if d == 'L':
        return pos[0], pos[1]-1
    if d == 'R':
        return pos[0], pos[1]+1


def show(knots, n=50):
    canvas = [['.' for i in range(n)] for j in range(n)]
    for i in range(10):
        k = knots[i]
        m = 'H' if i == 0 else str(i)
        canvas[k[0]-n//2][k[1]-n//2] = m

    for i in range(len(canvas)):
        print(''.join(canvas[i]))

def solve(num=9):
    knots = [[0,0] for i in range(1+num)]
    vis = set()


    def follow(h, t):
        t = t.copy()
        if h[0] - t[0] > 1:
            t[0] += 1
            t[1] += min((h[1]-t[1]), 1) if h[1]-t[1] >= 0 else max((h[1]-t[1]), -1)
        elif h[0] - t[0] < -1:
            t[0] -= 1
            t[1] += min((h[1]-t[1]), 1) if h[1]-t[1] >= 0 else max((h[1]-t[1]), -1)
        elif h[1] - t[1] > 1:
            t[1] += 1
            t[0] += min((h[0]-t[0]), 1) if h[0]-t[0] >= 0 else max((h[0]-t[0]), -1)
        elif h[1] - t[1] < -1:
            t[1] -= 1
            t[0] += min((h[0]-t[0]), 1) if h[0]-t[0] >= 0 else max((h[0]-t[0]), -1)
        return t

    for row in data.strip().split('\n'):
        d, n = row.split(' ')
        for i in range(int(n)):
            knots[0] = move(knots[0], d)
            for j in range(1, num+1):
                knots[j] = follow(knots[j-1], knots[j])

            vis.add(tuple(knots[-1]))


    return len(vis)


print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(9))


