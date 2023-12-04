# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:27:16 2023

@author: gape
"""

from collections import Counter, defaultdict
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(4, year=2023)
print('Day 4 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


data = [d for d in data.strip().split('\n')]


def process(row, copies):
    a, b = row.split(': ')
    n = int(a[5:])
    games = b.split(' | ')
    winning = [int(i) for i in games[0].split()]
    mine = [int(i) for i in games[1].split()]

    points = 0
    wins = 0
    for i in mine:
        if i in winning:
            wins += 1
            if points == 0:
                points = 1
            else:
                points *= 2


    for i in range(wins):
        copies[n+i+1] += copies[n]

    return points



total_points = 0
copies = Counter()
for i, row in enumerate(data):
    copies[i+1] += 1
    total_points += process(row, copies)

print("Task 1 answer:", total_points)
print("Task 2 answer:", sum(copies.values()))


