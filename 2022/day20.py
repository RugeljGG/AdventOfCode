# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:06:33 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import math
from functools import cmp_to_key
from itertools import cycle
import re

import numpy as np
import scipy as sp
import scipy.optimize
import aoc_helper


data = aoc_helper.get_input(20, year=2022)
print('Day 20 input:')
print(data[:100])
print('Total input length: ', len(data))

# data = """1
# 2
# -3
# 3
# -2
# 0
# 4"""

def solve(part=1):
    key = 811589153 if part == 2 else 1

    files = [(i, int(v)*key) for i, v  in enumerate(data.strip().split('\n'))]

    l = len(files)

    for mix in range(10 if part == 2 else 1):
        # print([f[1] for f in files])
        i = 0
        to_pop = 0
        while i < len(files):
            offset = 0
            while True:
                if files[(i-offset)% l][0] == to_pop:
                    i = (i-offset)% l
                    break
                elif files[(i+offset)%l][0] == to_pop:
                    i = (i+offset)%l
                    break
                else:
                    offset += 1

            index, v = files.pop(i)
            files.insert((i+v)%(l-1), (index, v))
            to_pop = index + 1
            # print(v, [f[1] for f in files])
            if to_pop >= l:
                break

    # print([f[1] for f in files])

    for i, v in enumerate(files):
        if v[1] == 0:
            break

    s = 0
    for j in range(1,4):
        s += files[(i+j*1000)%len(files)][1]

    return s

print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))
