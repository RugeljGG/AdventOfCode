# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:30:01 2018

@author: Gape
"""

import copy
from collections import defaultdict

class Unit():
    def __init__(self, x, y, team, data):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
        self.alive = True
        self.team = team
        self.data = data
        if team == 'E':
            self.data.elves.append(self)
            self.opposite = 'G'
        else:
            self.data.goblins.append(self)
            self.opposite = 'E'
        self.data.units.append(self)
        self.data.alive[team]+=1
        
        
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y and self.x < other.x:
            return True
        else:
            return False

    def move(self):
        if self.data.alive[self.opposite] <= 0:
            return -1
        possible = self.adjacent()
        targets = []
        for coords, s in possible:
            if isinstance(s, Unit) and s.team != self.team:
                targets.append(s)
        if not targets:
            best_path = self.find_nearest()
            if best_path is None:
                return 0
            self.data.zone[self.y][self.x] = '.'
            self.x, self.y = best_path[1]
            self.data.zone[self.y][self.x] = self
            possible = self.adjacent()
            for coords, s in possible:
                if isinstance(s, Unit) and s.team != self.team:
                    targets.append(s)
        if targets:
            targets = sorted(targets, key = lambda x: (x.hp, x.y, x.x))
            targets[0].get_hit(self.ap)
        
        return 1
        
    def get_hit(self,ap):
        self.hp -= ap
        if self.hp <= 0:
            self.alive = False
            self.data.zone[self.y][self.x] = '.'
            self.data.alive[self.team] -= 1
            if self.team == 'E':
                self.data.elf_dead = True
    
    def find_nearest(self):
        searched = set()
        paths = [[(self.x, self.y)]]
        while paths:
#            print(paths)
            new_paths = []
            for path in paths:
                x, y = path[-1]
                possible = self.adjacent((x,y))
                for coords, s in possible:
                    if coords in searched:
                        continue
                    searched.add(coords)
                    if s == '.':
                        new_paths.append(path+[coords])
                    elif isinstance(s, Unit) and s.team != self.team:
                        path.append(coords)
                        return path
            paths = new_paths
                        
            
    def adjacent(self, coords=None):
        adj = []
        zone = self.data.zone
        if coords is None:
            x, y = self.x, self.y
        else:
            x, y = coords
        if y > 0:
            adj.append(((x, y-1), zone[y-1][x]))
        if x > 0:
            adj.append(((x-1, y),zone[y][x-1]))
        if x < len(zone[0])-1:
            adj.append(((x+1, y),zone[y][x+1]))
        if y < len(zone)-1:
            adj.append(((x, y+1),zone[y+1][x]))
        return adj

    def __repr__(self):
        return '{}: {} hp ({},{})'.format(self.team, self.hp, self.x, self.y)


def show_zone(zone):
    for row in zone:
        s = ''.join(c if isinstance(c, str) else c.team for c in row)
        adder = ''.join(c.__repr__() for c in row if isinstance(c, Unit))
        print(s + '    ' + adder)

class Data():
    def __init__(self, alive, zone, elves, goblins, units):
        self.alive = alive
        self.zone = zone
        self.elves = elves
        self.goblins = goblins
        self.units = units
        self.elf_dead = False

def task1():
    alive = defaultdict(int)
    zone = []
    elves = []
    goblins = []
    units = []
    data = Data(alive, zone, elves, goblins, units)
    with open('day15.txt') as file:
        for y, row in enumerate(file):
            data.zone.append([])
            for x, c in enumerate(row.strip()):
                if c in ('E', 'G'):
                    c = Unit(x, y, c, data)
                data.zone[-1].append(c)
    
    rounds = 0
    cont = 1
    while cont:
#        print(rounds)
    #    show_zone(data.zone)
        data.units.sort()
        cont = 0
        for unit in data.units:
            if unit.alive:
                res = unit.move()
                if res == -1:
                    cont = 0
                    break
                elif res > 0:
                    cont = 1
        if not cont:
            break
        rounds += 1
    #    s = input()
    #    if s == 'b':
    #        break
        
    total_hp = sum(unit.hp for unit in data.units if unit.alive)
    return (total_hp, rounds, rounds* total_hp)


def task2():
    alive = defaultdict(int)
    zone = []
    elves = []
    goblins = []
    units = []
    data = Data(alive, zone, elves, goblins, units)
    with open('day15.txt') as file:
        for y, row in enumerate(file):
            data.zone.append([])
            for x, c in enumerate(row.strip()):
                if c in ('E', 'G'):
                    c = Unit(x, y, c, data)
                data.zone[-1].append(c)
                
    original = data
    
    ap = 3
    while True:
        data = copy.deepcopy(original)
        ap += 1
        print(ap)
        data.elf_dead = False
        for elf in data.elves:
            elf.ap = ap
        rounds = 0
        cont = 1
        while cont:
#            print(rounds)
#            show_zone(data.zone)
            data.units.sort()
            cont = 0
            for unit in data.units:
                if unit.alive:
                    res = unit.move()
                    if data.elf_dead:
                        cont = 0
                        break
                    if res == -1:
                        cont = 0
                        break
                    elif res > 0:
                        cont = 1
            if not cont:
                break
            rounds += 1
#            s = input()
#            if s == 'b':
#                break
        if not data.elf_dead:
            break
        
    total_hp = sum(unit.hp for unit in data.units if unit.alive)
    return (total_hp, rounds, rounds* total_hp)