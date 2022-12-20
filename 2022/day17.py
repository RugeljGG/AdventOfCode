# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 05:59:53 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(17, year=2022)
print('Day 17 input:')
print(data[:100])
print('Total input length: ', len(data))

data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


shapes = [((0,0), (1,0), (2,0), (3,0)),
          ((0,-1), (1,-1), (1,-2), (2,-1), (1,0)),
          ((0,0), (1,0), (2,0), (2,-1), (2,-2)),
          ((0,0), (0,-1), (0,-2), (0,-3)),
          ((0,-1), (1,-1), (0,0), (1,0)),]


def show(taken, new, floor, stop=0):
    for row in range(floor-8, stop):
        print('|', end='')
        for col in range(7):
            if (col, row) in taken:
                c = '#'
            elif (col, row) in new:
                c = '@'
            else:
                c = ' '
            print(c, end='')
        print('|')
    print('+-------+')
    print()


def find_shape(taken, floor):
    shape = []
    for col in range(7):
        row = 0
        while True:
            if (col, row+floor) in taken:
                shape.append(row)
                break
            else:
                row += 1
    return tuple(shape)

def solve(limit):
    taken = set()

    rocks = []
    moves = {'<': (-1, 0),
             '>': (1, 0)}

    floor = 0
    for i in range(7):
        taken.add((i, floor))

    pattern = cycle(data.strip())
    l = len(data.strip())
    pi = 0

    cycles = dict()

    r = -1
    adder = 0
    repeat_count = Counter()

    while r < limit-1:
        r += 1

        # print(floor)
        shape = shapes[r%5]

        if adder == 0:
            token = (r%5, pi%l, find_shape(taken, floor))
            if token in cycles:
                r1, pi1, f1 = cycles[token]
                if repeat_count[token] >= 2:
                    mul = (limit - r) // (r-r1)
                    adder = (floor-f1) * mul
                    r += mul * (r-r1)
                else:
                    repeat_count[token] += 1
            else:
                cycles[token] = [r, pi, floor]

        rock = [(i+2, j+floor-4) for i, j in shape]
        for c in pattern:
            pi += 1
            move = moves[c]
            new = []
            for pos in rock:
                n1 = (pos[0]+move[0], pos[1])
                if n1 in taken or n1[0]<0 or n1[0]>6:
                    break
                else:
                    new.append(n1)
            else:
                rock = new

            # show(taken, rock, floor)
            new2 = []
            for pos in rock:
                n2 = (pos[0], pos[1]+1)
                if n2 in taken:
                    break
                else:
                    new2.append(n2)
            else:
                rock = new2
                # show(taken, rock, floor)
                continue

            rocks.append(rock)
            for pos in rock:
                taken.add(tuple(pos))
                if pos[1] < floor:
                    floor = pos[1]

            break

    return -(adder+floor)

print("Task 1 answer:", solve(2022))
print("Task 2 answer:", solve(1000000000000))


