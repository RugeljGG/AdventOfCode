# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 19:55:02 2022

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


data = aoc_helper.get_input(19, year=2022)
print('Day 19 input:')
print(data[:100])
print('Total input length: ', len(data))

# data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

blueprints = dict()
for row in data.strip().split('\n'):
    nums = [int(i) for i in re.findall(pattern, row)[0]]
    num = nums[0]
    costs = ((nums[1], 0, 0, 0), (nums[2], 0, 0, 0), (nums[3], nums[4], 0, 0), (nums[5], 0, nums[6], 0))
    blueprints[num] = costs

def solve(part=1):
    minutes = 32 if part == 2 else 24
    power_levels = []
    for k, costs in blueprints.items():
        c = [0] * minutes * 3 + list(range(-minutes+1,1))

        bounds = [(0, 1) for i in range(minutes*4)]

        A_ub = []
        b_ub = []
        for m in range(minutes):
            for ore in range(4):  # sum of production must be higher than consumption
                cost = [+costs[j][ore] if m>=i else 0  for j in range(4) for i in range(minutes)]  # cost to build
                production = [-max((m-i-1, 0)) if j == ore else 0  for j in range(4) for i in range(minutes)]
                A_ub.append([x+y for x,y in zip(cost, production)])
                limit = m if ore == 0 else 0  # one ore robot at start
                b_ub.append(limit)

            # only one factory per turn
            A_ub.append([1 if m==i else 0 for j in range(4) for i in range(minutes)])
            b_ub.append(1)

        res = sp.optimize.linprog(c, A_ub, b_ub, bounds=bounds, integrality=np.ones_like(c), method='highs')
        if part == 1:
            power_levels.append(k * -res.fun)
        else:
            power_levels.append(-res.fun)
            if k == 3:
                break

    if part == 1:
        return int(sum(power_levels))
    else:
        return int(math.prod(power_levels))

print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))

