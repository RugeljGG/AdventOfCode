# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:48:52 2023

@author: gape
"""

from collections import Counter, defaultdict
from functools import cache
import re
import pandas as pd
import aoc_helper

data = aoc_helper.get_input(12, year=2023)
print('Day 12 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


# data = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """

data = [d for d in data.strip().split('\n')]


@cache
def check(s, previous, current, records):
    if not len(s):
        return len(records) == 0 and (current is None or current[0] == current[1])

    if not len(records) and current is None and '#' in s:
        return False

    c = s[0]
    if c == '.':
        if current is not None and current[0] != current[1]:
            return False
        else:
            return check(s[1:], '.', None, records)

    elif c == '#':
        if current is not None:
            current = current[0], current[1] + 1
            if current[1] > current[0]:
                return False
        elif len(records) == 0:
            return False
        else:
            current = records[0], 1
            records = records[1:]
        return check(s[1:], '#', current, records)

    else:
        return (check('.' + s[1:], previous, current, records) +
                check('#' + s[1:], previous, current, records)
                )



def solve(part=1):
    counts = 0
    for i, row in enumerate(data):
        # print(i, flush=True)
        s, nums = row.split(' ')
        if part == 2:
            s = '?'.join([s]*5)
            nums = ','.join([nums]*5)
        nums = tuple(int(i) for i in nums.split(','))

        counts += check(s, None, None, nums)

    return counts

print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))

