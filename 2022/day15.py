# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 09:25:37 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(15, year=2022)
print('Day 15 input:')
print(data[:100])
print('Total input length: ', len(data))

# data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


sensor_data = []
for row in data.strip().split('\n'):
    ptrn = "Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"
    nums = re.findall(ptrn, row)[0]
    x1, y1, x2, y2 = (int(i) for i in nums)
    d =  abs(y2-y1) + abs(x2-x1)
    sensor_data.append((x1, y1, x2, y2, d))


empty = set()
for x1, y1, x2, y2, distance in sensor_data:
    for y in range(-distance, distance+1):
        yn = y1 + y
        if yn == 2000000:
            for x in range(-distance+abs(y), distance+1-abs(y)):
                xn = x1 + x
                if abs(y) + abs(x) <= distance and (xn, yn) != (x2, y2):

                    empty.add((xn, yn))

print("Task 1 answer:", len(empty), flush=True)



limit = 4000000
for y in range(limit, -1, -1):
    # if y % 100000 == 0:
    #     print(y, flush=True)
    possible = deque([(0, limit)])
    for x1, y1, x2, y2, d in sensor_data:
        d_available = d-abs(y-y1)
        x_d = x1-d_available
        x_u = x1+d_available
        new = list()
        for xmin, xmax in possible:
            if xmax < x_d:
                new.append((xmin, xmax))
            elif xmin > x_u:
                new.append((xmin, xmax))
            elif xmin < x_d and xmax <= x_u:
                new.append((xmin, x_d-1))
            elif xmin < x_d and xmax >= x_u:
                new.append((xmin, x_d-1))
                new.append((x_u+1, xmax))
        possible = new
    if len(possible):
        print("Task 2 answer:", (possible[0][0] * 4000000) + y)
        break


