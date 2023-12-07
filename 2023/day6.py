# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:16:42 2023

@author: gape
"""


from collections import Counter, defaultdict
import math
import re

import pandas as pd

import aoc_helper

data = aoc_helper.get_input(6, year=2023)
print('Day 6 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()



data = [d for d in data.strip().split('\n')]


def f_slow(time_lim, distance):  # original function
        counter = 0
        for speed in range(1, time_lim+1):
            time_left = time_lim - speed
            if distance / speed < time_left:
                counter += 1
        return counter

def f_fast(time_lim, distance):  # much more elegant :)
    d = (time_lim**2 - 4*distance)**0.5
    start = math.ceil((time_lim - d)/2)
    end = math.floor((time_lim + d)/2)
    return end-start+1

def solve(data, part=1):

    if part == 1:
        times = [int(i) for i in data[0].split(':')[1].strip().split()]
        distances  =  [int(i) for i in data[1].split(':')[1].strip().split()]
    else:
        times = [int(data[0].split(':')[1].replace(' ', ''))]
        distances  =  [int(data[1].split(':')[1].replace(' ', ''))]


    counters = []
    for i in range(len(times)):
        time_lim = times[i]
        distance = distances[i]
        counters.append( f_fast(time_lim, distance))

    return pd.Series(counters).prod()


print("Task 1 answer:", solve(data, 1))
print("Task 2 answer:", solve(data, 2))
