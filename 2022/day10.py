# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:25:31 2022

@author: gape
"""


from collections import Counter, defaultdict, deque
import numpy as np
import re

import aoc_helper

data = aoc_helper.get_input(10, year=2022)
print('Day 10 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

x = 1
buffer = [0, 0]

i = 0
strength = 0
buffer = dict()

image = [[' ' for col in range(40)] for row in range(6)]
for row in data.strip().split('\n'):
    cmd = row.split()
    if cmd[0] == 'noop':
        move = 1
    elif cmd[0] == 'addx':
        buffer[i+2] = int(cmd[1])
        move = 2

    for j in range(move):
        i += 1
        if i in (20, 60, 100, 140, 180, 220):
            strength += i* x

        row = (i-1)//40
        col = (i-1)%40
        if abs(col - x) <= 1:
            image[row][col] = '#'

        if i in buffer:
            x += buffer[i]

print("Task 1 answer:", strength)
print("Task 2 answer:")


for row in image:
    print(''.join(row))

