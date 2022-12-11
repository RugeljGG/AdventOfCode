# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 05:59:38 2022

@author: gape
"""


from collections import Counter, defaultdict, deque
import numpy as np
import re

import aoc_helper

data = aoc_helper.get_input(11, year=2022)
print('Day 11 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


def task1():
    monkeys = dict()
    for monkey in data.strip().split('\n\n'):
        mdata = monkey.split('\n')
        mid = int(re.findall('\d+', mdata[0])[0])
        nums = deque(int(i) for i in mdata[1].split(': ')[1].split(','))
        formula = mdata[2].split(': ')[1][6:]
        div = int(mdata[3].split(' ')[-1])
        tr = int(mdata[4].split(' ')[-1])
        fl = int(mdata[5].split(' ')[-1])

        monkeys[mid] = [nums, formula, div, [tr, fl]]

    counts = Counter()

    for i in range(20):
        print(i, flush=True)
        for j, monkey in monkeys.items():
            while len(monkey[0]):
                counts[j] += 1
                old = monkey[0].popleft()
                new = eval(monkey[1])//3
                if new % monkey[2] == 0:
                    mid = monkey[3][0]
                else:
                    mid = monkey[3][1]
                monkeys[mid][0].append(new)

    s = sorted(counts.values())
    return (s[-1]*s[-2])


def task2():
    monkeys = dict()
    divs = list()
    for monkey in data.strip().split('\n\n'):
        mdata = monkey.split('\n')
        mid = int(re.findall('\d+', mdata[0])[0])
        nums = deque(int(i) for i in mdata[1].split(': ')[1].split(','))
        formula = mdata[2].split(': ')[1][6:]
        if formula == 'old * old':
            fm = ['old']
        elif '+' in formula:
            fm = ['+',  int( formula.split('+')[1])]
        else:
            fm = ['*',  int(formula.split('*')[1])]
        div = int(mdata[3].split(' ')[-1])
        divs.append(div)
        tr = int(mdata[4].split(' ')[-1])
        fl = int(mdata[5].split(' ')[-1])

        monkeys[mid] = [nums, fm, div, [tr, fl]]

    counts = Counter()

    for m, monkey in monkeys.items():
        for j in range(len(monkey[0])):
            item = monkey[0].popleft()
            c = Counter()
            for div in divs:
                c[div] = item % div
            monkey[0].append(c)



    for i in range(10000):
        for j, monkey in monkeys.items():
            while len(monkey[0]):
                counts[j] += 1
                item = monkey[0].popleft()

                formula = monkey[1]
                if formula[0] == 'old':
                    new = Counter({k:(v*v)%k for k, v in item.items()})
                elif formula[0] == '+':
                    new =  Counter({k:(v+formula[1])%k for k, v in item.items()})
                elif formula[0] == '*':
                    new =  Counter({k:(v*formula[1])%k for k, v in item.items()})
                if new[monkey[2]] == 0:
                    mid = monkey[3][0]
                else:
                    mid = monkey[3][1]
                monkeys[mid][0].append(new)

    s = sorted(counts.values())
    return (s[-1]*s[-2])

print("Task 1 answer:", task1())
print("Task 2 answer:", task2())

