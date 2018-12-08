# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 08:48:43 2018

@author: Gašper Rugelj
"""

from collections import defaultdict
import re


def task1():
    before = defaultdict(list)
    after = defaultdict(list)

    with open('day7.txt') as file:
        for row in file:
            res = re.findall('Step (.) must be finished before step (.) can begin.', row)
            a, b = res[0]
            after[a].append(b)
            len(before[a])
            before[b].append(a)

    order = []


    available = []
    while True:
        for i, values in before.items():
            if len(values) == 0:
                available.append(i)
        for i in available:
            try:
                before.pop(i)
            except KeyError:
                pass
        if len(available) == 0:
            break
        available.sort()
        i = available.pop(0)
        order.append(i)
        for j in after[i]:
            before[j].remove(i)

    return ''.join(order)

def task2(fn='day7.txt', num=5, seconds=60):
    adder = seconds + 1 - ord('A')

    before = defaultdict(list)
    after = defaultdict(list)

    with open(fn) as file:
        for row in file:
            res = re.findall('Step (.) must be finished before step (.) can begin.', row)
            a, b = res[0]
            after[a].append(b)
            len(before[a])
            before[b].append(a)

    available = []

    workers = [[None, None] for i in range(num)]

    time = 0
    order = []
    while True:
        time += 1
        space = []
        working = False
#        print(workers)
        for i, worker in enumerate(workers):
            if worker[0] is None:
                space.append(i)
            else:
                working = True
                if worker[1] <= 1:
                    for j in after[worker[0]]:
                        before[j].remove(worker[0])
                    order.append(worker[0])
                    worker[0] = None
                    worker[1] = None
                    space.append(i)
                else:
                    worker[1] -= 1

        if not space:
            continue # če ni workerjev ni treba računati!


        for i, values in before.items():
            if len(values) == 0:
                available.append(i)
        for i in available:
            try:
                before.pop(i)
            except KeyError:
                pass
        if len(available) == 0:
            if working:
                continue
            else:
                break
    #    print(available)
        available.sort()
        while space and available:
            i = available.pop(0)
            j = space.pop(0)
            worker = workers[j]
            worker[0] = i
            worker[1] = ord(i) + adder

    return time - 2