# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 05:58:30 2019

@author: gape
"""

from collections import defaultdict


def task1():
    lab = []
    with open('day24.txt') as file:
        for row in file:
            lab.append([c for c in row.strip()])

    seen = dict()
    count = 0
    while True:
        new_lab = []
        for row in lab:
            new_lab.append(row.copy())
        for y in range(len(lab)):
            for x in range(len(lab)):
                c = lab[y][x]
                num = 0
                for n in [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]:
                    nx, ny = n
                    if nx<0 or ny<0 or nx>len(lab[0])-1 or ny>len(lab)-1:
                        continue
                    nc = lab[ny][nx]
                    if nc == '#':
                        num += 1
                if c == '.' and num in (1,2):
                    new_lab[y][x] = '#'
                elif c == '#' and num != 1:
                    new_lab[y][x] = '.'


        lab = new_lab
        key = ''.join([''.join(row) for row in lab])
        count+=1
        if key in seen:

            rating = 0
            for i, c in enumerate(key):
                if c == '#':
                    rating += 2**i
            break
        else:
            seen[key] = count
    return rating


class Point():
    def __init__(self, c, x, y, l):
        self.c = c
        self.x = x
        self.y = y
        self.l = l
        self.infested = 0

    def infest(self, points, levels=True):
        x, y, l0 = self.x, self.y, self.l
        neighbours = []
        for nx, ny in [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]:
            l = l0
            if levels and nx == 2 and ny == 2:
                l-=1
                if x == 1:
                    nx = 0
                    for ny in range(5):
                        neighbours.append((nx, ny, l))
                elif x == 3:
                    nx = 4
                    for ny in range(5):
                        neighbours.append((nx, ny, l))
                elif y == 1:
                    ny = 0
                    for nx in range(5):
                        neighbours.append((nx, ny, l))
                elif y == 3:
                    ny = 4
                    for nx in range(5):
                        neighbours.append((nx, ny, l))
            else:
                if nx<0:
                    ny = 2
                    nx = 1
                    l+=1
                elif ny<0:
                    ny = 1
                    nx = 2
                    l+=1
                elif nx>4:
                    ny = 2
                    nx = 3
                    l+=1
                elif ny>4:
                    ny = 3
                    nx = 2
                    l+=1
                if l == 0 or levels:
                    neighbours.append((nx, ny, l))
        for k in neighbours:
            nx, ny, l = k
            if k not in points:
                points[k] = Point('.', nx, ny, l)
            points[k].infested += 1

    def morph(self, bugs):
        if self.c == '.' and self.infested in (1,2):
            self.c = '#'
            bugs[(self.x, self.y, self.l)] = self
        elif self.c == '#' and self.infested != 1:
            self.c = '.'
            bugs.pop((self.x, self.y, self.l))
        self.infested = 0


def show(points):
    levels = defaultdict(lambda: [['.' for i in range(5)] for j in range(5)])
    for p in points.values():
        levels[p.l][p.y][p.x] = p.c

    for l, lab in sorted(levels.items(), key=lambda x: x[0]):
        print("level: ", l)
        for row in lab:
            print(''.join(row))

def task2(debug=False):
    lab = []
    with open('day24.txt') as file:
        for row in file:
            lab.append([c for c in row.strip()])


    points = dict()
    bugs = dict()
    for y in range(len(lab)):
        for x in range(len(lab)):
            c = lab[y][x]
            p = Point(c, x, y, 0)
            points[(x,y, 0)] = p
            if c == '#':
                bugs[(x,y, 0)] = p

    if debug:
        show(points)
    for i in range(200):
        for bug in bugs.values():
            bug.infest(points)
        for p in points.values():
            p.morph(bugs)
        if debug:
            print()
            print("Time = ", i+1)
            show(points)

    return len(bugs)

print("Task 1 answer: ", task1())
print("Task 2 answer: ", task2())