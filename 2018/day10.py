# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 05:59:06 2018

@author: Gape
"""

import re 

class Star():
    def __init__(self, p, v):
        self.x = p[0]
        self.y = p[1]
        self.vx = v[0]
        self.vy = v[1]
        
    def move(self, t=1):
        self.x += self.vx
        self.y += self.vy

stars = []
with open('day10.txt') as file:
    for row in file:
        r = re.findall('position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>', row)
        p = int(r[0][0]), int(r[0][1])
        v = int(r[0][2]), int(r[0][3])
        stars.append(Star(p,v))

space = [['.' for i in range(240)] for j in range(80)]
seconds = 0
while True:
    seconds+=1
    move = False
    xmax = -99999
    xmin = 99999
    ymax = -99999
    ymin = 99999
    for star in stars:
        if star.x > xmax:
            xmax = star.x
        if star.x < xmin:
            xmin = star.x
        if star.y > ymax:
            ymax = star.y
        if star.y < ymin:
            ymin = star.y
#    print(xmax, xmin, ymax, ymin)
    if (xmax - xmin < 240) and (ymax - ymin < 80):
        move = True
    for star in stars:
        star.move()
        if move:
            j, i = star.x, star.y
            space[i-ymin][j-xmin] = '#'
    if move:
        print(seconds)
        for row in space:
            print(''.join(row))
        s = input()
        if 'b' in s:
            break
        for star in stars:
            j, i = star.x, star.y
            space[i-ymin][j-xmin] = '.'