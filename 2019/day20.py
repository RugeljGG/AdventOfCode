# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:59:39 2019

@author: gape
"""

from collections import deque

class Point():
    def __init__(self, x, y, c, points, n=None):
        self.x = x
        self.y = y
        self.c = c
        self.n = dict()
        self.neighbours = []
        self.portal_coords = dict()
        self.points = points
        
    def __repr__(self):
        return self.c + '({},{})'.format(self.x, self.y)
    
    def find_neighbours(self):
        x, y = self.x, self.y
        for ns in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if ns in self.points:
                self.neighbours.append((self.points[ns], 0))
        
    def portal(self):
        x, y = self.portal_coords[True]
        for ns in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if ns in self.points:
                self.neighbours.append((self.points[ns], 0))
        if False in self.portal_coords:
            x, y = self.portal_coords[False]
            for ns in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                if ns in self.points:
                    self.neighbours.append((self.points[ns], 0))
            self.neighbours[0][0].neighbours.append((self.neighbours[1][0], -1))
            self.neighbours[1][0].neighbours.append((self.neighbours[0][0], 1))
                
    def spread(self, n, l, movers):
        if l < 0:
            return False
        if l in self.n and n >= self.n[l]:
            return False
        else:
            self.n[l] = n
        for nb, ln in self.neighbours:
            movers.append((nb,n+1,l+ln))

lab = []
with open('day20.txt') as file:
    for row in file:
        lab.append([c for c in row.strip('\r\n')])

def run(use_levels=False):
    points = dict()
    portals = dict()
    for y in range(len(lab)-1):
        for x in range(len(lab[y])-1):
            yp = y
            c = lab[y][x]
            if c == '.':
                points[(x,y)] = Point(x,y,c, points)
            elif c.isupper():
                outer = True
                if lab[y][x+1].isupper():
                    ch = c + lab[y][x+1]
                    if x < len(lab[y]) -2 and lab[y][x+2] == '.':
                        x = x+1
                        if x > 2:
                            outer = False
                    elif (len(lab[y]) - x) > 2:
                        outer = False
                elif lab[y+1][x].isupper():
                    ch = c + lab[y+1][x]
                    if y < len(lab)-2 and lab[y+2][x] == '.':
                        yp = y+1
                        if y > 2:
                            outer = False
                    elif (len(lab) - y) > 2:
                        outer = False
                else:
                    continue
                if ch in portals:
                    portals[ch].portal_coords[outer] = x, yp
                else:
                    p = Point(x,yp,ch, points)
                    portals[ch] = p
                    p.portal_coords[outer] = x, yp
                    
    for point in points.values():
        point.find_neighbours()
        
    for portal in portals.values():
        portal.portal()
    
    start = portals['AA'].neighbours[0][0]
    target = portals['ZZ'].neighbours[0][0]
    movers = deque([(start, 0, 0)])
    while movers:
        p, n, l = movers.popleft()
        if p is target and l == 0:
#            print(n)
            break
        else:
            if not use_levels:
                l = 0
            p.spread(n, l, movers)
    return n

print("Task 1:", run())
print("Task 2:", run(True))