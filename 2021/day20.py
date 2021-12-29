# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:35:46 2021

@author: gape
"""

from collections import Counter, defaultdict, deque
from math import ceil, floor
import re

import aoc_helper

data = aoc_helper.get_input(20, year=2021).strip()

print('Day 20 input:')
print(data[:200])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()


# data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###"""

data = data.split('\n')

algo = data[0].replace('#', '1').replace('.', '0')

s_img = data[2:]

pixels = dict()

for y, row in enumerate(s_img):
    for x, c in enumerate(row):
        i = '1' if c == '#' else '0'
        pixels[(x,y)] = i


def find_pixels(x,y):
    return ((x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),   (x, y),   (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
            )
    

def show(pixels):
    min_x = min(pixels, key=lambda x:x[0])[0]
    max_x = max(pixels, key=lambda x:x[0])[0]
    min_y = min(pixels, key=lambda x:x[1])[1]
    max_y = max(pixels, key=lambda x:x[1])[1]
    for y in range(min_y-1, max_y+2):
        row = []
        for x in range(min_x-1, max_x+2):
            v=pixels.get((x,y), '0')
            c = '#' if v == '1' else ' '
            row.append(c)
        print(''.join(row))
    print()


old = pixels
for step in range(50):
    min_x = min(pixels, key=lambda x:x[0])[0]
    max_x = max(pixels, key=lambda x:x[0])[0]
    min_y = min(pixels, key=lambda x:x[1])[1]
    max_y = max(pixels, key=lambda x:x[1])[1]

    # show(pixels)
    new = dict()
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            temp = []
            for x_n, y_n in find_pixels(x,y):
                default = '0' if step % 2 == 0 else '1'
                temp.append(pixels.get((x_n, y_n), default))
            new[(x,y)] = algo[int(''.join(temp), 2)]
    pixels = new
    if step == 1:
        print("Part 1 answer:", sum((int(i) for i in pixels.values())))
        
    if step == 49:
        print("Part 2 answer:", sum((int(i) for i in pixels.values())))
    
    
# show(pixels)