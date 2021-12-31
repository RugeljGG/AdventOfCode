# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:15:13 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(24, year=2021).strip()

print('Day 24 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

parts = [p.strip().split('\n') for p in data.split('inp w\n')[1:]]

pattern = """inp w
mul x 0
add x z
mod x (-?\d*?)
div z (-?\d*?)
add x (-?\d*?)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (-?\d*?)
mul y x
add z y"""


def formula(inputs, w, z):
    if w == (z % inputs[0] + inputs[2]):
        z = int(z/(inputs[1]))
    else:
        z = int(z/(inputs[1]))
        z*=26
        z += w+inputs[3]
    return z


rows = re.findall(pattern,data)
rows = [[int(j) for j in row] for row in rows]

correct = defaultdict(set)
correct[13] = set((0,))

for i in range(13,-2, -1):
    # print(i)
    inputs = rows[i]
    for c in correct[i]:
        for w in range(1, 10):
            d1 = (c - inputs[3] - w)
            remain = w - inputs[2]
            if d1 % 26 == 0:
                if inputs[1] == 1:
                    if d1 % 26 == remain:
                        continue
                    else:
                        correct[i-1].add(int(d1/26))
                else:
                    if d1 == 0:
                        rng = range(-25, 26)
                    else:
                        s = int(abs(d1)/d1)
                        rng = range(d1, d1+26*s, s)

                    for t in rng:
                        if t % 26 == remain:
                            continue
                        correct[i-1].add(t)
            if remain < 0:
                continue
            elif inputs[1] == 1:
                if c % inputs[0] == remain:
                    correct[i-1].add(c)
            else:
                if c>=0:
                    correct[i-1].add(c*26+remain)
                if c<=0:
                    if remain:
                        remain = remain - 26
                    correct[i-1].add(c*26+remain)


def solve(asc=False):
    rng = range(1, 10, 1) if asc else range(9, 0, -1)
    z = 0
    model = []
    for i in range(14):
        inputs = [int(j) for j in rows[i]]
        for w in rng:
            z_n = formula(inputs, w, z)
            if z_n in correct[i]:
                z = z_n
                model.append(w)
                break
    return ''.join((str(i) for i in model))

print("Part 1 answer:", solve(False))
print("Part 2 answer:", solve(True))