# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:15:07 2023

@author: gape
"""

from collections import Counter, defaultdict, deque
from functools import cache
import re
import pandas as pd
import aoc_helper
import networkx as nx

data = aoc_helper.get_input(19, year=2023)
print('Day 19 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


w, p = data.strip().split('\n\n')

pattern = "(.*?){(.*?)}"
pp = "{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}"
p2 = '(\D)([<>])(\d+)'

rules = dict()
for row in w.split('\n'):
    name, r = re.findall(pattern, row)[0]
    rules[name] = [i.split(':') for i in r.split(',')]

def solve1():
    def check(part, rules):
        x, m, a, s = part
        n = 'in'
        while n not in ('A', 'R'):
            rule = rules[n]
            for r in rule:
                if len(r) == 1:
                    n = r[0]
                else:
                    if eval(r[0]):
                        n = r[1]
                        break
        if n == 'A':
            return x+m+a+s
        elif n == 'R':
            return 0
        else:
            raise


    suma = 0
    for part in p.split('\n'):
        part = (int(i) for i in re.findall(pp, part)[0])
        suma += check(part, rules)
    return suma



def solve2():
    options = [{'pos': 'in',
                'x':(1,4000),
                'm':(1,4000),
                'a':(1,4000),
                's':(1,4000),
                },
               ]

    count = 0
    while len(options):
        opt = options.pop()
        n = opt['pos']
        if n == 'A':
            c = 1
            for k, v in opt.items():
                if k != 'pos':
                    c *= (v[1] - v[0] + 1)
            count += c
        elif n == 'R':
            continue
        elif isinstance(n, str):
            opt['pos'] = rules[n]
            options.append(opt)
        elif isinstance(n, list):
            r = n[0]
            if len(r) == 1:
                opt['pos'] = r[0]
                options.append(opt)
            else:
                k, s, v  = re.findall(p2, r[0])[0]
                v = int(v)
                rng = opt[k]
                if s == '>':
                    if rng[0] > v:
                        opt['pos'] = r[1]
                        options.append(opt)
                    elif rng[1] <= v:
                        opt['pos'] = n[1:]
                        options.append(opt)
                    else:
                        opt1 = opt.copy()
                        opt2 = opt.copy()

                        opt1[k] = (rng[0], v)
                        opt2[k] = (v+1, rng[1])

                        options.append(opt1)
                        options.append(opt2)

                elif s == '<':
                    if rng[1] < v:
                        opt['pos'] = r[1]
                        options.append(opt)
                    elif rng[0] >= v:
                        opt['pos'] = n[1:]
                        options.append(opt)
                    else:
                        opt1 = opt.copy()
                        opt2 = opt.copy()

                        opt1[k] = (rng[0], v-1)
                        opt2[k] = (v, rng[1])

                        options.append(opt1)
                        options.append(opt2)


    return count

print("Task 1 answer:", solve1())
print("Task 2 answer:", solve2())

