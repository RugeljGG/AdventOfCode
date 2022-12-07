# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 05:58:55 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
import re

import aoc_helper

data = aoc_helper.get_input(7, year=2022)
print('Day 7 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


dirs = list()

lim = 100000
max_size = 70000000 - 30000000

class Dir:
    def __init__(self, name, upper):
        self.lower = dict()
        self.upper = upper
        self.files = dict()
        self.size = 0
        dirs.append(self)

    def calc(self):
        c = 0
        for l in self.lower.values():
            c += l.calc()
        c+= sum(self.files.values())
        self.size = c
        return c


main = Dir('/', None)
cdir = None

for row in data.split('\n')[:-2]:
    cmds = (row).split()
    if cmds[0] == '$':
        if cmds[1] == 'cd':
            if cmds[2] == '..':
                cdir = cdir.upper
            elif cmds[2] == '/':
                cdir = main
            else:
                if cmds[2] not in cdir.lower:
                    cdir.lower[cmds[2]] = Dir(cmds[2], cdir)
                cdir = cdir.lower[cmds[2]]
    elif cmds[0] == 'dir':
        if cmds[1] not in cdir.lower:
            cdir.lower[cmds[1]] = Dir(cmds[1], cdir)
    else:
        if cmds[1] not in cdir.files:
            cdir.files[cmds[1]] = int(cmds[0])

main.calc()
print("Task 1 answer:", sum((d.size if d.size<lim else 0 for d in dirs)))

req =  main.size  - max_size

for d in sorted(dirs, key=lambda x:x.size):
    if d.size >= req:
        print("Task 2 answer:", d.size)
        break
