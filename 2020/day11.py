# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 05:59:32 2020

@author: gape
"""

from collections import Counter
import re

import aoc_helper

data = aoc_helper.get_input(11, force=True).strip()
# data = aoc_helper.get_input(11).strip()
print('Day 11 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


def count1(i_s, j_s, data):
    cnt = 0
    for j in range(j_s-1, j_s+2):
        if j < 0 or j > len(data)-1:
            continue
        else: 
            row = data[j]
            for i in range(i_s-1, i_s+2):
                if i < 0 or i > len(row)-1 or (j==j_s and i==i_s):
                    continue
                else:
                    if row[i] == '#':
                        cnt +=1
    return cnt
   

moves = ((0,1),
         (1,1),
         (1,0),
         (1,-1),
         (0,-1),
         (-1,-1),
         (-1,0),
         (-1,1),)

def count2(i_s, j_s, data):
    cnt = 0
    
    for i_m, j_m in moves:
        i = i_s
        j = j_s
        while True:
            i += i_m
            j += j_m
            if i<0 or i>len(data[0])-1 or j<0 or j>len(data)-1:
                break
            elif data[j][i] == '#':
                cnt+=1
                break
            elif data[j][i] == 'L':
                break
            else:
                continue
    return cnt


def solve(data, fun, lim):
    curr = [[c for c in row] for row in data.split()]
    while True:
        old = [[a for a in row] for row in curr]
        changes = 0
        for i in range(len(old[0])):
            for j in range(len(old)):
                if old[j][i] == 'L' and fun(i, j, old) == 0:
                    curr[j][i] = '#'
                    changes += 1
                elif old[j][i] == '#' and fun(i, j, old) >= lim:
                    curr[j][i] = 'L'
                    changes += 1
                else:
                    continue
        if changes == 0:
            break
    s = '\n'.join([''.join(row) for row in curr])
    return s.count('#')
    
            
print("Part 1 answer: ", solve(data, count1, 4))
print("Part 2 answer: ", solve(data, count2, 5))     