# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 05:59:31 2020

@author: gape
"""


import copy
from collections import Counter, defaultdict
import re

import aoc_helper

data = aoc_helper.get_input(20, force=True).strip()
# data = aoc_helper.get_input(20).strip()
print('Day 20 input (first 10 lines):')
print('\n'.join(data.split('\n')[:10]))
print('\nTotal input length: ', len(data))
print('Total input row count: ', len(data.split('\n'))-1)
print("\n############################################################\n")

def show_i(image, rotation, xflip, yflip, pp=True, gaps=True):
    size = 10 if gaps else 8
    data = [[' ' for x in range(size)] for j in range(size)]
    xs, xe = (0, size) if gaps else (1, size+1)
    ys, ye = (0, size) if gaps else (1, size+1)
    gap = 0 if gaps else 1
    for xi in range(xs, xe):
        for yi in range(ys, ye):

            if xflip:
                x = 9-xi
            else:
                x = xi
            if yflip:
                y = 9-yi
            else:
                y = yi


            if rotation == 0:
                xr = x
                yr = y
            if rotation == 1:
                xr = 9-y
                yr = x
            if rotation == 2:
                xr = 9-x
                yr = 9-y
            if rotation == 3:
                xr = y
                yr = 9-x
            data[yr-gap][xr-gap] = image[yi][xi]

    if pp:
        for row in data:
            print(''.join(row))
    else:
        return data

def show(locations, rows=132, cols=132, gaps=True, ret=False):
    if gaps:
        split = 1
    else:
        split = 0
    data = [[' ' for x in range(cols)] for j in range(rows)]
    for k, v in locations.items():
        xs, ys, (rotation, xflip, yflip) = v

        image = images[k]

        partial = show_i(image, rotation, xflip, yflip, False, gaps)

        size = 10 if gaps else 8
        y0 = ys*(size+split)
        x0 = xs*(size+split)

        for yp, row in enumerate(partial):
            data[y0+yp][x0:x0+size] = row

    if ret:
        return data
    else:
        for row in data:
            print(''.join(row))


images = dict()

for image in data.split('\n\n'):
    img = []
    for j, row in enumerate(image.split('\n')):
        if j == 0:
            c_id = int(re.findall('\d+', row)[0])
        else:
            img.append([c for c in row])
    images[c_id] = img

corners = dict()
corners_r = dict()
for k, v in images.items():
    top = []
    for i in range(len(v[0])):
        c = v[0][i]
        if c == '#':
            top.append(i)
    bottom = []
    for i in range(len(v[0])):
        c = v[-1][i]
        if c == '#':
            bottom.append(i)
    left = []
    for j in range(len(v)):
        c = v[j][0]
        if c == '#':
            left.append(j)
    right = []
    for j in range(len(v[0])):
        c = v[j][-1]
        if c == '#':
            right.append(j)
    corners[k] = [top, right, bottom, left]


correct = []
pairs = defaultdict(list)
for k, v in corners.items():
    count = 0
    for k2, v2 in corners.items():
        if k2 == k:
            continue
        for i in range(4):
            for j in range(4):
                if v[i] == v2[j]:
                    count+=1
                    pairs[k].append((k2, i, j, 0))
                    break
                elif v[i] == [9 - xi for xi in v2[j][::-1]]:
                    count+=1
                    pairs[k].append((k2, i, j, 1))
                    break
            else:
                continue
            break
    if count == 2:
        correct.append(k)
    # print(k, count)

num = 1
for c in correct:
    num*=c

print("part 1 answer:", num)

locations = dict()

if correct[0] == 1951:

    locations[correct[0]] = 0, 0, (1, 0, 0)
    cache = [[correct[0], 1, 0, 0]]
else:
    locations[correct[0]] = 0, 0, (0, 0, 0)
    cache = [[correct[0], 0, 0, 0]]

taken_coords = []

used = dict()
errors = defaultdict(list)
while len(pairs):
    k, rotation, xflip, yflip = cache.pop()
    candidates = pairs.pop(k)
    used[k] = candidates
    x, y, _ = locations[k]
    for c in candidates:
        kc, kp, kr, kf = c
        if kc in locations:
            continue

        kxflip = 0
        kyflip = 0
        if kr == 0:
            kxflip = (kp in (0,1)) ^ kf
        if kr == 2:
            kxflip = (kp in (2,3)) ^ kf
        if kr == 1:
            kyflip = (kp in (0,1)) ^ kf
        if kr == 3:
            kyflip = (kp in (2,3)) ^ kf

        if kr % 2 == 0:
            kxflip =  kxflip ^ xflip ^ yflip
        elif kr % 2 == 1:
            kyflip =  kyflip ^ yflip ^ xflip


        if xflip and kp%2 == 1:
            kp = (kp+2)%4
        if yflip and kp%2 == 0:
            kp = (kp+2)%4

        krotation = (kp - kr - 2)%4
        krotation = (krotation+rotation)%4
        kposition = (kp+rotation)%4

        if kposition == 0:
            ky = y-1
            kx = x
        if kposition == 1:
            kx = x+1
            ky = y
        if kposition == 2:
            ky = y+1
            kx = x
        if kposition == 3:
            ky = y
            kx = x-1

        if kx < 0 or kx > 11 or ky<0 or ky>11:
            errors[k].append((kc, kx, ky))
            continue

        if (kx, ky) in taken_coords:
            errors[k].append((kc, kx, ky))
            continue

        locations[kc] = kx, ky, (krotation, kxflip, kyflip)
        taken_coords.append((kx, ky))
        cache.append([kc, krotation, kxflip, kyflip])

    # show(locations, rows=max(taken_coords, key=lambda x:x[1])[1]*10+20)
    # c = input()
    # if c == 'c':
    #     break

monster = """                  # \n#    ##    ##    ###\n #  #  #  #  #  #   """.split('\n')
monster_coords = []
for j in range(3):
    for i in range(20):
        if monster[j][i] == '#':
            monster_coords.append((i,j))

def print_monster(coords):
    canvas = [[' ' for x in range(20)] for j in range(20)]
    for x, y in coords:
        canvas[y][x] = '#'
    for row in canvas:
        print(''.join(row))

monsters = dict()
for xflip in (0, 1):
    for yflip in (0,1):
        hmonster = []
        vmonster = []
        for x, y in monster_coords:
            if xflip:
                x = 20-x
            if yflip:
                y = 20-y
            hmonster.append((x,y))
            vmonster.append((y,x))

        monsters[(xflip, yflip, 0)] = (hmonster)
        monsters[(xflip, yflip, 1)] = (vmonster)

size = int(len(locations)**0.5*8)
data = show(locations, cols=size, rows=size, gaps=False, ret=True)

counts = dict()

for xflip in (0, 1):
    for yflip in (0,1):
        for hv in (0,1):
            good_positions = []
            m = monsters[(xflip, yflip, hv)]
            for xs in range(-20, size):
                for ys in range(-20, size):
                    for xm, ym in m:
                        x = xs+xm
                        y = ys+ym
                        if x >= size or y >= size:
                            break
                        elif data[y][x] != '#':
                            break
                    else:
                        for xm, ym in m:
                            x = xs+xm
                            y = ys+ym
                            data[y][x] = 'o'
                        good_positions.append((xs, ys, num))
            counts[(xflip, yflip, hv)] = len(good_positions)

print("Part 2 answer:", sum([''.join(row).count('#') for row in data]))

for row in data[::-1]:
    print('\033[34m'+''.join(row[::-1]).replace('o', '\033[31mo\033[34m'))