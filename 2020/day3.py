# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 04:56:48 2020

@author: gape
"""


import aoc_helper

data = aoc_helper.get_input(3, force=True)

print('Day 3 input:')
print(data)
print('Total input length: ', len(data))
print('Total input row length: ', len(data.split('\n'))-1)
print()

data = [row for row in data.split('\n') if row != '']

count = 0
i = 0
for row in data[1:]:
    i+=3
    i = i%len(row)
    if row[i] == '#':
        count+=1

print("Part 1 answer: ", count)

mul = 1
for j in (1, 3, 5, 7):
    count = 0
    i = 0
    for row in data[1:]:
        i+=j
        i = i%len(row)
        if row[i] == '#':
            count+=1
    print(count)
    mul*=count
    

count = 0
i = 0
for row in data[2::2]:
    i+=1
    i = i%len(row)
    if row[i] == '#':
        count+=1
# print(count)
mul*=count

print("Part 2 answer: 2", mul)