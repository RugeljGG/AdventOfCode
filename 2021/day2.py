# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 05:57:22 2021

@author: gape
"""

import aoc_helper

data = aoc_helper.get_input(2, year=2021, force=True).strip()

print('Day 2 input:')
print(data[:100])
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split()))
print()

data = data.split('\n')


def task1():

    def move(d,i):
        i = int(i)
        if d == 'down':
            return 0, +i
        if d == 'up':
            return 0, -i
        if d == 'forward':
            return i, 0
        
    x, y = 0, 0
    for row in data:
        xm, ym = move(*row.split(' '))
        x += int(xm)
        y += int(ym)
        
    return x*y
        

def task2():
    
    x, y = 0, 0
    aim = 0
    for row in data:
        d, i = row.split(' ')
        i = int(i)
        if d == 'down':
            aim += i
        if d == 'up':
            aim -= i
        if d == 'forward':
            x += i
            y += aim * i
            
    return x*y

print("Task 1:", task1())
print("Task 2:", task2())