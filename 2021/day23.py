# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:50:55 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(23, year=2021).strip()

print('Day 23 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

class Slot:
    def __init__(self, isroom, ishallway, name):
        self.isroom = isroom
        self.ishallway = ishallway
        self.neigh = []
        self.name = name
        self.paths = dict()

    def find_destination(self, prev):
        path = prev+[self.name]
        if len(prev) and prev[0][0] == 'R' and self.name[0] != 'R':
            self.paths[prev[0]] = path[::-1]
        paths = []
        if not self.ishallway:
            paths.append(path)
        for n in self.neigh:
            if n.name not in prev:
                paths += n.find_destination(path)
        return paths

    def __repr__(self):
        return str(self.name)


def move(pods, pods_r, rooms_c, cost, memory, locations, best=None, r_size=2):
    best_path = None
    correct = 0
    for pod, pos in pods.items():
        if pod[0] == pos[1] and (rooms_c[pos[1]] > (r_size-int(pos[2]))):
                correct += 1
                continue
        for dest, path in locations[pos].paths.items():
            if dest[0] == 'R' and dest[1] != pod[0]:  # only move into correct room
                continue
            elif dest[0] == 'H' and pos[0] == 'H':  # can't move from hallway to hallway
                continue
            elif dest[0] == 'R' and (rooms_c[dest[1]] < (r_size-int(dest[2]))):  # don't move into first position in room if occupied by wrong pod/empty
                continue
            elif (set(pods_r) & set(path[1:])):  # don't move if path is taken
                continue
            else:
                pods_n = pods.copy()
                pods_r_n = pods_r.copy()
                rooms_c_n = rooms_c.copy()
                pods_n[pod] = dest
                pods_r_n.pop(pos)
                pods_r_n[dest] = pod
                if dest[0] == 'R':
                    rooms_c_n[dest[1]] += 1
                if pos[0] == 'R' and pos[1] == pod[0]:
                    rooms_c_n[pos[1]] -= 1
                cost_n = cost + (len(path)-1) * costs[pod[0]]
                if best is not None and cost_n >= best:
                    continue
                hsh = tuple(sorted(pods_n.items()))
                if hsh in memory and memory[hsh] <= cost_n:
                    continue
                else:
                    memory[hsh] = cost_n
                candidate, c_path = move(pods_n, pods_r_n, rooms_c_n, cost_n, memory, locations, best, r_size)
                if c_path is not None and (best is None or candidate < best):
                    best = candidate
                    best_path = [(pod, dest)] + c_path
                    if candidate == cost:
                        return best, best_path
    if correct == len(pods):
        best = cost
        best_path = []
        # print("Solved!", best)
    return best, best_path



def solve(data, rows=2):

    slots = dict(H1=Slot(False, False, 'H1'))

    for i in range(10):
        name = 'H'+str(i+2)
        slots[name] = (Slot(False,False, name))
        slots[name].neigh.append(slots['H'+str(i+1)])
        slots['H'+str(i+1)].neigh.append(slots[name])
    rooms = dict()
    names = 'ABCD'
    for i in range(4):
        for j in range(rows):
            name = 'R'+names[i]+str(j+1)
            rooms[name] = Slot(True, False, name)
            if j == 0:
                h = slots['H' + str(3+i*2)]
                h.neigh.append(rooms[name])
                h.ishallway = True
                rooms[name].neigh.append(h)
            else:
                name2 =  'R'+names[i]+str(j)
                rooms[name].neigh.append(rooms[name2])
                rooms[name2].neigh.append(rooms[name])


    for room in rooms.values():
        paths = room.find_destination([])
        for path in paths:
            if path[-1] != room.name:
                room.paths[path[-1]] = path

    pods = dict()
    count = Counter()
    for row in data:
        for c in row:
            if c in names:
                count[c] += 1
                name = c + str(count[c])
                pos = len(pods)*rows % (4* rows)+ len(pods)//4
                pods[name] = list(rooms.values())[pos].name

    pods_r = {v:k for k, v in pods.items()}

    both = rooms.copy()
    both.update(slots)


    memory = dict()

    rooms_c = Counter()
    for pod, pos in pods.items():
        if pos[0] == 'R' and pod[0] == pos[1]:
            rooms_c[pos[1]] += 1

    return move(pods, pods_r, rooms_c, 0, memory, both, None, rows)[0]


# data = """
# #############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########"""

extra_data = """#D#C#B#A#
  #D#B#A#C#"""

p1_data = data.split('\n')
extra_data = extra_data.split('\n')
p2_data = p1_data[:-2] + extra_data + p1_data[-2:]

costs = dict(A=1,
            B=10,
            C=100,
            D=1000)

print("Part 1 answer", solve(p1_data, 2))
print("Part 2 answer", solve(p2_data, 4))