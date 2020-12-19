# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 05:59:42 2020

@author: gape
"""

import copy
from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(19, force=True).strip()
# data = aoc_helper.get_input(19).strip()
print('Day 19 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

rules_raw = dict()
r, msgs = data.split('\n\n')
for row in r.split('\n'):
    k, v = row.split(': ')
    rls = v.split(' | ')
    rules_raw[int(k)] = []
    for rv in rls:
        if '"' in rv:
            rules_raw[int(k)].append([rv[1]])
        else:
            rules_raw[int(k)].append([int(c) for c in rv.split()])

def parse(i, part=1):
    if part==2 and i in (11, 8):
        return ['_{}_'.format(i)]

    r = rules_raw[int(i)]
    rls = []
    for rl in r:
        if isinstance(rl[0], str):
            return [rl[0]]
        else:
            if len(rl) == 1:
                for rl1 in parse(rl[0], part=part):
                    rls.append(rl1)
            else:
                for rl1 in parse(rl[0], part=part):
                    for rl2 in parse(rl[1], part=part):
                        try:
                            rls.append(rl1+rl2)
                        except:
                            print(i)
                            raise
    return rls
    # return '|'.join([','.join(r) for r in rls])

t1 = parse(42)
t2 = parse(31)
num = len(t1[0])

count = 0

for msg in msgs.split():
    if len(msg)==num*3 and msg[:num] in t1 and  msg[num:num*2] in t1 and msg[num*2:num*3] in t2:
        count+=1

print("Part 1 answer:", count)

count = 0
correct = []
for msg in msgs.split():
    i = 0
    phase1 = True
    c1 = 0
    c2 = 0
    while i < len(msg):
        if phase1:
            if msg[i:i+num] in t1:
                i += num
                c1 += 1
                continue
            else:
                phase1 = False
        else:
            if msg[i:i+num] in t2:
                i += num
                c2 += 1
            else:
                break
    else:
        if i==len(msg) and c2>0 and c1 > c2:
            count+=1

print("Part 2 answer:", count)