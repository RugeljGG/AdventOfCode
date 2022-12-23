# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 06:59:35 2022

@author: gape
"""

from collections import Counter, defaultdict, deque
from itertools import cycle
import numpy as np
import re

from functools import cmp_to_key
import aoc_helper


data = aoc_helper.get_input(22, year=2022)
print('Day 22 input:')
print(data[:100])
print('Total input length: ', len(data))

def show():
    for y in range(len_y):
        row = []
        for x in range(len_x):
            if (x,y) in traversed:
                c = '>'
            else:
                c = board_map.get((x,y), ' ')
                if c == '.':
                    c = ' '
            row.append(c)
        print(''.join(row))



p1, p2, _ = data.split('\n\n')

board_map = dict()

for y, row in enumerate(p1.split('\n')):
    for x, c in enumerate(row):
        if c != ' ':
            board_map[(x, y)] = c


def jump(pos, direction):
    x, y = pos
    while True:
        x = (x + direction[0]) % len_x
        y = (y + direction[1]) % len_y
        if (x,y) in board_map:
            break

    return x, y

# transfer: left, top, right, down
def transfer_side(pos, direction):
    # input positions:
    #   _01
    #   _2_
    #   34_
    #   5__

    x, y = pos
    # side 0
    # left -> 3 iz leve
    if x == 50 and y >= 0 and y < 50 and direction == (-1,0):
        d_n = (1,0)
        x_n = 0
        y_n = 100 + (49-y)

    # top -> 5 iz leve
    if x >= 50 and x < 100 and y == 0 and direction == (0,-1):
        d_n = (1,0)
        x_n = 0
        y_n = 150 + (x-50)

    # side 1
    # top -> 5 od spodaj
    if x >= 100 and x < 150 and y == 0 and direction == (0,-1):
        d_n = (0,-1)
        x_n = x - 100
        y_n = 199
    # right -> 4 iz desne
    if x == 149 and y >= 0 and y < 50 and direction == (1,0):
        d_n = (-1,0)
        x_n = 99
        y_n = 100 + (49-y)
    # down -> 2 iz desne
    if x >= 100 and x < 150 and y == 49 and direction == (0,1):
        d_n = (-1,0)
        x_n = 99
        y_n = 50 + (x-100)

    # side 2
    # left -> 3 od zgoraj
    if x == 50 and y >= 50 and y < 100 and direction == (-1,0):
        d_n = (0, 1)
        x_n = y - 50
        y_n = 100

    # right -> 1 od spodaj
    if x == 99 and y >= 50 and y < 100 and direction == (1,0):
        d_n = (0, -1)
        x_n = 100 + y - 50
        y_n = 49

    # side 3
    # left -> 0 iz leve
    if x == 0 and y >= 100 and y < 150 and direction == (-1,0):
        d_n = (1,0)
        x_n = 50
        y_n = (149-y)

    # top -> 2 iz leve
    if x >= 0 and x < 50 and y == 100 and direction == (0,-1):
        d_n = (1,0)
        x_n = 50
        y_n = 50 + x

    # side 4
    # right -> 1 iz desne
    if x == 99 and y >= 100 and y < 150 and direction == (1,0):
        d_n = (-1,0)
        x_n = 149
        y_n = (149-y)

    # bottom -> 5 iz desne
    if x >= 50 and x < 100 and y == 149 and direction == (0, 1):
        d_n = (-1,0)
        x_n = 49
        y_n = 150 + (x-50)


    # side 5
    # left -> 0 od zgoraj
    if x == 0 and y >= 150 and y < 200 and direction == (-1,0):
        d_n = (0,1)
        x_n = 50 + (y-150)
        y_n = 0

    # right -> 4 od spodaj
    if x == 49 and y >= 150 and y < 200 and direction == (1, 0):
        d_n = (0,-1)
        x_n = 50 + (y-150)
        y_n = 149

    # bottom -> 1 od zgoraj
    if  x >= 0 and x < 50 and y == 199 and direction == (0, 1):
        d_n = (0,1)
        x_n = 100 + x
        y_n = 0


    return x_n, y_n, d_n

# side_position = ((None,0,1),
#                  (None,2, None),
#                  (3,4, None),
#                  (5, None, None))


# side_transfers = {0: ((3, (1,0), "y obratno",),
#                       (5, (1,0), "x = y",),
#                       (1, (1,0), "nič sprememb",),
#                       (2, (0,1), "nič sprememb",),
#                       )
#                   }


path = re.findall(('\d+|\D+'), p2)

turns = {'L': {(1,0): (0,-1),
               (0,-1): (-1,0),
               (-1,0): (0,1),
               (0,1): (1,0),
               },
         'R': {(1,0): (0,1),
               (0,1): (-1,0),
               (-1,0): (0,-1),
               (0,-1): (1,0),
            }
         }

value = {(1,0): 0,
         (0,1): 1,
         (-1, 0): 2,
         (0, -1):3,
    }


len_x = max(board_map, key=lambda x: x[0])[0]+1
len_y = max(board_map, key=lambda x: x[1])[1]+1


start_x = min(x for (x,y), v in board_map.items() if y==0  and v != ' ')

def solve(part=1):
    pos = (start_x, 0)
    direction = (1,0)

    traversed = set()
    traversed.add(pos)
    for c, p in enumerate(path):
        # print(c, p, pos, direction, flush=True)
        # if c == 3:
        #     break

        # if c % 10 == 0 and c!= 0:
            # show()
            # input()
        try:
            p = int(p)
            i = 0
            while i < p:
                x, y = pos[0]+direction[0],pos[1]+direction[1]

                dir_n = direction
                if (x,y) not in board_map:
                    if part == 2:
                        x, y, dir_n = transfer_side(pos, direction)
                    else:
                        x, y = jump(pos, direction)
                        dir_n = direction

                c = board_map.get((x, y))
                if c == '#':
                    break

                if (x,y) == (0, 201):
                    raise
                pos = x, y
                direction = dir_n
                traversed.add(pos)
                i+=1


        except ValueError:
            direction = turns[p][direction]

    result = (pos[1]+1) * 1000 + (pos[0]+1) * 4 + value[direction]
    return result


print("Task 1 answer:", solve(1))
print("Task 2 answer:", solve(2))

