# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:58:43 2018

@author: Gape
"""

import copy

#zone = []
#with open('day18.txt') as file:
#    for row in file:
#        zone.append(list(row.strip()))
        
def roll(x,y, zone):
    if x>0:
        if y > 0:
            yield zone[y-1][x-1]
        yield zone[y][x-1]
        if y < len(zone) -1:
            yield zone[y+1][x-1]
    if y > 0:
        yield zone[y-1][x]
        if x < len(zone[0])-1:
            yield zone[y-1][x+1]
    if x < len(zone[0])-1:
        yield zone[y][x+1]
        if y < len(zone) -1:
            yield zone[y+1][x+1]
    if y < len(zone) -1:
        yield zone[y+1][x]
        
def display(zone):
    for row in zone:
        print(''.join(row))
        
#total = 10 # part 1

#total = 1000000000 # part 2


def calculate(total, zone):
    previous = dict()
    for t in range(total):
    #    print(t)
    #    display()
        new = copy.deepcopy(zone)
        for y in range(len(zone)):
            for x in range(len(zone[0])):
                c = zone[y][x]
                if c == '.':
                    counter = 0
                    for o in roll(x,y, zone):
                        if o == '|':
                            counter += 1
                            if counter >= 3:
                                new[y][x] = '|'
                                break
                if c == '|':
                    counter = 0
                    for o in roll(x,y, zone):
                        if o == '#':
                            counter += 1
                            if counter >= 3:
                                new[y][x] = '#'
                                break
                if c == '#':
                    counter1 = False
                    counter2 = False
                    for o in roll(x,y, zone):
                        if o == '|':
                            counter1 = True
                        if o == '#':
                            counter2 = True
                        if counter1 and counter2:
                            break
                    else:
                        new[y][x] = '.'
        hashed = ''.join(c for row in zone for c in row)
        if hashed in previous.keys():
#            print(previous[hashed])
            break
        else:
            previous[hashed] = t
            zone = new
    return zone, previous, hashed, t


def task1():
    zone = []
    with open('day18.txt') as file:
        for row in file:
            zone.append(list(row.strip()))
    zone, _, _, _ = calculate(10, zone)
    tr = sum(1 for row in zone for c in row if c == '|')
    lum = sum(1 for row in zone for c in row if c == '#')
    return tr * lum
    
def task2():
    zone = []
    with open('day18.txt') as file:
        for row in file:
            zone.append(list(row.strip()))
    total = 1000000000   
    zone, previous, hashed, t = calculate(total, zone)
    num = (t - previous[hashed])
    remaining = (total - t) % num
    zone, previous, hashed, t = calculate(remaining, zone)
    tr = sum(1 for row in zone for c in row if c == '|')
    lum = sum(1 for row in zone for c in row if c == '#')
    return tr * lum