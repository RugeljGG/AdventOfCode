# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 15:58:26 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(24, year=2022)
print('Day 24 input:')
print(data[:100])
print('Total input length: ', len(data))


# data = """#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#"""

def show(blizzards_history, path):
    for i in range(len(blizzards_history)):
        # print("minute", i)
        blizzards = blizzards_history[i]
        pos = path[i]
        if pos in blizzards:
            raise
        print('#'*(max_x+3))
        for y in range(max_y+1):
            row = ['#']
            for x in range(max_x+1):
                bs = blizzards[(x, y)]
                if len(bs) > 1:
                    c = str(len(bs))
                elif len(bs) == 1:
                    c = bs[0]
                elif pos == (x,y):
                    c = 'E'
                else:
                    c = '.'
                row.append(c)
            row.append('#')
            print(''.join(row))
        print('#'*(max_x+3))
        print()


moves = {'^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0),
        '0': (0,0),
        }

def move_blizzards(blizzards):
    new_blizzards = defaultdict(list)
    for (x,y), bs in blizzards.items():
        for b in bs:
            move = moves[b]
            x_new = (x + move[0]) % (max_x+1)
            y_new = (y + move[1]) % (max_y+1)
            new_blizzards[x_new, y_new].append(b)

    return new_blizzards

def find_path(start, end, blizzards):
    t = 0
    options = {start:[start]}
    blizzards_history = [blizzards]
    while end not in options:
        t+=1
        # print(t)


        blizzards = move_blizzards(blizzards)
        new_options = dict()
        for (x,y), path in options.items():
            for move in moves.values():
                x_new = x + move[0]
                y_new = y + move[1]
                if (x_new, y_new) not in blizzards:
                    if ((x_new, y_new) in (start, end) or
                        (x_new >= 0 and x_new <= max_x and y_new>=0 and y_new<=max_y)
                        ):
                        new_options[(x_new, y_new)] = path + [(x_new, y_new)]


        options = new_options
        blizzards_history.append(blizzards)

    best_path = options[end]

    return t, best_path, blizzards



blizzards = defaultdict(list)
for y, row in enumerate(data.strip().split('\n')[1:-1]):
    for x, c in enumerate(row[1:-1]):
        if c in moves:
            blizzards[(x,y)].append(c)


max_x = max(blizzards, key=lambda x: x[0])[0]
max_y = max(blizzards, key=lambda x: x[1])[1]


start = (0, -1)
end = (max_x, max_y+1)


total_t = 0
t, best_path, blizzards = find_path(start, end, blizzards)
total_t += t

print("Task 1 answer:", t)

t, best_path, blizzards = find_path(end, start, blizzards)
total_t += t
t, best_path, blizzards = find_path(start, end, blizzards)
total_t += t

print("Task 2 answer:", total_t)