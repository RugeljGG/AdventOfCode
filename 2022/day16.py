# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:29:05 2022

@author: gape
"""


from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(16, year=2022)
print('Day 16 input:')
print(data[:100])
print('Total input length: ', len(data))


# data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""


class Valve:
    def __init__(self, vid, flow, targets, valves):
        self.vid = vid
        self.flow = flow
        self.targets = targets
        # self.scores = defaultdict(dict)
        self.scores = dict()
        self.paths = dict()
        self.valves = valves

    def tell_path(self, durations):
        durations = durations.copy()
        for k, v in durations.items():
            if self.flow > 0:
                duration = min(self.valves[k].paths.get(self.vid, 9999), v+1)
                self.valves[k].paths[self.vid] = duration
            durations[k] += 1

        durations[self.vid] = 0

        for target in self.targets:
            if target not in durations:
                self.valves[target].tell_path(durations)

    def calc_path(self, origin, time, durations):

        durations[self.vid] = time
        if self.flow > 0 and self.vid != origin:
            self.valves[origin].paths[self.vid] = time

        for target in self.targets:
            if target not in durations or durations[target] > time+1:
                self.valves[target].calc_path(origin, time+1, durations)



    def search(self, opened, score, time):

        if time <= 0:
            return []


        key = frozenset(opened)
        if key in self.scores and self.scores[key] >= score:
            return []

        else:
            self.scores[key] = score

        options = deque()
        if self.flow > 0 and self.vid not in opened:
            new_opened = opened.union([self.vid])
            options.append((self.vid, new_opened, score+self.flow*(time-1), time-1))

        for target, duration in self.paths.items():

            options.append((target, opened, score, time-duration))


        return options


def solve(part=1):

    valves = dict()
    available = 0
    max_len = 0
    for row in data.strip().split('\n'):
        pattern = "Valve (\D\D) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
        parsed = re.findall(pattern, row)[0]
        vid = parsed[0]
        flow = int(parsed[1])
        available += flow
        targets = parsed[2].split(', ')
        valves[vid] = Valve(vid, flow, targets, valves)
        if flow >= 0:
            max_len += 1


    start = 'AA'
    time = 30 if part == 1 else 26


    for k, v in valves.items():
        if k == start or v.flow > 0:
            v.calc_path(k, 0, dict())



    queues = defaultdict(deque)

    queues[time].append((start, set(), 0, time))
    scores = Counter()

    for t in range(time, 0, -1):
        queue = queues[t]
        # print(t, len(queue))


        while queue:
            vid, opened, score, time = queue.popleft()
            key = frozenset(opened)
            if scores[key] < score:
                scores[key] = score
            new = valves[vid].search(opened, score, time)
            for n in new:
                t1 = n[3]
                queues[t1].append(n)

    best = max(scores.items(), key=lambda x: x[1])[1]

    if part == 2:
        for k1, v1 in scores.items():
            for k2, v2 in scores.items():
                if v1+v2 > best and k1.isdisjoint(k2):
                    best = v1+v2

    return best


print("Task 1 answer:", solve(part=1))
print("Task 2 answer:", solve(part=2))