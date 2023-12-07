# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:46:17 2023

@author: gape
"""

from collections import Counter, defaultdict
import math
import re

import pandas as pd

import aoc_helper

data = aoc_helper.get_input(7, year=2023)
print('Day 7 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

# data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

data = [d for d in data.strip().split('\n')]

power = 'AKQJT98765432'

def type_power(h, use_joker=False):

    if 'J' in h and use_joker:
        replacers = set(h)
        hs = []
        for r in replacers:
            hs.append(h.replace('J', r))
    else:
        hs = [h]

    best = 0

    for h in hs:
        threes = set()
        pairs = set()
        for c in h:
            if h.count(c) == 5:
                best = max(best, 7)
                break
            elif h.count(c) == 4:
                best = max(best, 6)
                break
            elif h.count(c) == 3:
                threes.add(c)
            elif h.count(c) == 2:
                pairs.add(c)

        if len(threes):
            if len(pairs):
                best = max(best, 5)
            else:
                best = max(best, 4)
        elif len(pairs) == 2:
            best = max(best, 3)
        elif len(pairs) == 1:
            best = max(best, 2)
        else:
            best = max(best, 1)

    return best


def color_power(h, use_joker=False):
    ps = []
    for c in h:
        if c == 'J' and use_joker:
            p = len(power)
        else:
            p = power.find(c)
        ps.append(str(len(power)-p).zfill(2))
    return ''.join(ps)

def compare(h1, h2):
    p1 = type_power(h1)
    p2 = type_power(h2)

    if p1 == p2:
        return p1 > p2
    else:
        return p1 > p2


def solve(part=1):
    hands = []
    use_joker = False if part == 1 else True
    for row in data:
        h, bet = row.split(' ')
        hands.append([h, int(str(type_power(h, use_joker)) + color_power(h, use_joker)), int(bet)])

    winnings = 0
    for i, h in enumerate(sorted(hands, key=lambda x: x[1])):
        # print(h, h[2] * (i+1))
        winnings += h[2] * (i+1)

    return winnings


print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))
