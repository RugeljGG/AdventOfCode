# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 05:59:01 2020

@author: gape
"""


import copy
from collections import Counter, defaultdict, deque
import re

import aoc_helper
#
data = aoc_helper.get_input(23, force=True).strip()
# data = aoc_helper.get_input(23).strip()
print('Day 23 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")


class Cup():
    def __init__(self, i, num):
        self.i = i
        self.num = num
        self.left = None
        self.right = None


def solve(part=1):
    cups_i = dict()
    cups_num = dict()
    for i, c in enumerate(data):
        c = int(c)
        cup = Cup(i, int(c))
        cups_i[i] = cup
        cups_num[c] = cup

    for i in range(len(cups_i)):
        if i == 0:
            cups_i[i].left = cups_i[len(cups_i)-1]
            cups_i[i].right = cups_i[i+1]
        elif i == len(cups_i)-1:
            cups_i[i].left = cups_i[i-1]
            cups_i[i].right = cups_i[0]
        else:
            cups_i[i].left = cups_i[i-1]
            cups_i[i].right = cups_i[i+1]

    lowest = min(cups_num.keys())
    highest = max(cups_num.keys())
    c_cup = cups_i[0]

    if part == 2:
        i = len(cups_i)-1
        h = highest
        cup = cups_i[i]
        while i < 1e6-1:
            i+=1
            highest+=1
            n_cup = Cup(i, highest)
            cup.right = n_cup
            n_cup.left = cup
            cups_num[highest] = n_cup
            cup = n_cup

        c_cup.left = n_cup
        n_cup.right = c_cup

    n_moves = 100 if part == 1 else int(1e7)
    for move in range(n_moves):
        if part == 2 and move % 100000 == 0:
            print("\rSolving part 2 ... {}%".format(int(move/n_moves*100)),flush=True, end='')

        moved = []
        cup = c_cup

        for i in range(3):
            cup = cup.right
            moved.append(cup.num)

        cup = cup.right
        c_cup.right = cup
        cup.left = c_cup

        # c_cup.right = c_cups[(i+4)%len(cup_i)]
        l = c_cup.num-1
        if l < lowest:
            l = highest
        while l in moved:
            l-=1
            if l < lowest:
                l = highest
        # print(moved, l)

        d_cup = cups_num[l]
        l_cup = cups_num[moved[0]]
        r_cup = cups_num[moved[-1]]
        n_cup = d_cup.right

        d_cup.right = l_cup
        l_cup.left = d_cup
        r_cup.right = n_cup
        n_cup.left = r_cup

        c_cup = c_cup.right


    if part == 1:
        s_cup = cups_num[1]
        order = []
        while len(order) < len(cups_num):
            order.append(str(s_cup.num))
            s_cup = s_cup.right
        return ''.join(order)[1:]
    else:
        print("\rSolving part 2 ... 100%", flush=True)
        return cups_num[1].right.right.num * cups_num[1].right.num

print("Part 1 answer:", solve(part=1))
print()
print("Part 2 answer:", solve(part=2))

