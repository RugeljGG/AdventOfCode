o# -*- coding: utf-8 -*-
"""
Created on Fri Jan 1 16:56:12 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
from math import log
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(25, year=2022)
print('Day 25 input:')
print(data[:100])
print('Total input length: ', len(data))

# data = """1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122"""

s = 0
mapping = {'2': 2,
           '1': 1,
           '0': 0,
           '-': -1,
           '=': -2,
           }

reverse_mapping = {v:k for k,v in mapping.items()}

def convert(snafu):
    num = 0
    for e, c in enumerate(snafu[::-1]):
        if c in mapping:
            i = mapping[c]
n        else:
            i = int(c)
        num += i * (5**e)

    return num


def reverse(num):
    level = round(log(num, 5))
    snafu = []
    for i in range(level, -1, -1):
        div = 5 ** i
        min_num = num
        for j in range(i-1, -1, -1):
            min_num += 2 * (5 ** j)
        n = min_num // div
        num -= n * div
        snafu.append(reverse_mapping[int(n)])

    return ''.join(snafu)


decimal = sum((convert(row) for row in data.strip().split('\n')))
print("Final puzzle answer:", reverse(decimal))