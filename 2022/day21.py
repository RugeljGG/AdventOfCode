# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:01:41 2022

@author: gape
"""


from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(21, year=2022)
print('Day 21 input:')
print(data[:100])
print('Total input length: ', len(data))


# data = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32"""

values = dict()

to_calc = []
for row in data.strip().split('\n'):
    name, shout = row.split(': ')
    code =  shout.split()
    if len(code) == 1:
        values[name] = int(code[0])
    else:
        to_calc.append((name, code))


original = values.copy()
order = []

while True:
    # print(len(values), len(to_calc), flush=True)
    for i in range(len(to_calc)):
        i
        name, code = to_calc[i]

        v1, op, v2 = code
        if name in values:
            continue

        elif v1 not in values or v2 not in values:
            continue

        else:
            v = eval('{}{}{}'.format(values[v1], op, values[v2]))
            values[name] = v
            order.append((name, code))
            break

    if 'root' in values:
        break

print("Task 1 answer:", int(values['root']))


def calc(i):
    current_values = original.copy()
    current_values['humn'] = i
    for name, code in order[:-1]:
        v1, op, v2 = code
        v = eval('{}{}{}'.format(current_values[v1], op, current_values[v2]))
        current_values[name] = v

    v1, op, v2 = order[-1][1]

    return current_values[v1], current_values[v2]


i = 1000000

first0, second0 = calc(0)
first, second = calc(i)

delta = (first - first0) / i

while first != second:
    diff = second - first
    i += diff / delta
    first, second = calc(i)


print("Task 2 answer:", int(i))