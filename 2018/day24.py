# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 06:00:41 2018

@author: Gape
"""

import copy
from collections import defaultdict
import re

class Group():
    def __init__(self, hp, ap, dtype, units, priority, weak, immune, team, data, gid):
        self.gid = gid
        self.hp = hp
        self.ap = ap
        self.alive = True
        self.team = team
        self.priority = priority
        self.units = units
        self.data=data
        self.dtype = dtype
        self.weak = weak
        self.immune = immune
        if team == 'Immune':
            self.data.immune.append(self)
            self.opposite = data.infection
        else:
            self.data.infection.append(self)
            self.opposite = data.immune
        self.data.units.append(self)
        self.data.alive[team]+=1
        
        
    def __lt__(self, other):
        if self.ap * self.units > other.ap * other.units:
            return True
        elif self.ap * self.units == other.ap * other.units and self.priority > other.priority:
            return True
        else:
            return False

     
    def get_hit(self, other):
        dmg = other.ap * other.units * self.multiplier(other.dtype)
        
        self.units -= dmg // self.hp
        if self.units <= 0:
            self.alive = False
            self.data.alive[self.team] -= 1


    def set_target(self, targets):
        if len(targets):
            targets.sort(key=lambda x: (x.multiplier(self.dtype), x.ap*x.units), reverse=True)
            if targets[0].multiplier(self.dtype) == 0:
                self.target = None
            else:
                self.target = targets.pop(0)
        else:
            self.target = None
        
        
    
    def multiplier(self, dtype):
        if dtype in self.weak:
            return 2
        elif dtype in self.immune:
            return 0
        else:
            return 1
        
    def __repr__(self):
        s = '{} {}: {} u:{} ap (t: {}). {} dtype. I: {}; W: {}. Prio: {}'
        
        return s.format(self.team, self.gid, self.units, self.ap, self.ap*self.units,
                        self.dtype, self.immune, self.weak, self.priority)
                        

class Data():
    def __init__(self, alive, immune, infection, units):
        self.alive = alive
        self.immune = immune
        self.infection = infection
        self.units = units
        self.elf_dead = False
        
alive = defaultdict(int)
immune = []
infection = []
units = []
data = Data(alive, immune, infection, units)
pattern = '(\d*) units each with (\d*) hit points( \(.*\))? with an attack that does (\d*) (.*) damage at initiative (\d*)'
with open('day24.txt') as file:
    for row in file:
#        print(row)
        row = row.strip()
        if row == 'Immune System:':
            team = 'Immune'
            gid = 0
            continue
        elif row == 'Infection:':
            team = 'Infection'
            gid = 0
            continue
        elif len(row) == 0:
            continue
        res = re.findall(pattern, row)[0]
        units = int(res[0])
        hp = int(res[1])
        immunities = res[2]
        ap = int(res[3])
        dtype = res[4]
        priority = int(res[5])
        
        weak = []
        immune = []
        immunities = immunities.strip(' ()')
        for immun in immunities.split(';'):
            if immun == '':
                continue
            res = re.findall('(.*) to (.*)', immun)[0]
            dtypes = res[1].split(', ')
            if res[0].strip() == 'immune':
                immune = dtypes
            elif res[0].strip() == 'weak':
                weak = dtypes
            else:
                print('ERROR', res[0])
        
        Group(gid=gid, hp=hp, ap=ap, units=units, dtype=dtype, priority=priority,
              weak=weak, immune=immune, team=team, data=data)
        gid += 1
        


def calculcate(data, boost=0):
    data = copy.deepcopy(data)
    if boost > 0:
        for d in data.immune:
            d.ap += boost
    while data.alive['Immune'] and data.alive['Infection']:
        data.units.sort() # data selection
        target_immune = [g for g in data.immune if g.alive]
        target_infection = [g for g in data.infection if g.alive]
        for g in data.units:
            if not g.alive:
                continue
            if g.team == 'Infection':
                targets = target_immune
            else:
                targets = target_infection
            g.set_target(targets)
        
        data.units.sort(key=lambda x: x.priority, reverse=True)
        attacks = 0
        for g in data.units:
            if not g.alive or g.target is None:
                continue
            g.target.get_hit(g)
            attacks += 1
        if not attacks: # infinite loop
            break
    return data

def task1():
    results = calculcate(copy.deepcopy(data))
    return sum(d.units for d in results.units if d.alive)

def task2():
    a = 0
    b = 1000
    while True:
        boost = (b-a) // 2 + a
        results = calculcate(copy.deepcopy(data), boost=boost)
        if results.alive['Infection'] == 0:
            b = boost
        else:
    #        boost += 1
            a = boost
#        print(a, b, boost)
        if b-a == 1:
            break
    if results.alive['Infection'] > 0:
         results = calculcate(copy.deepcopy(data), boost=boost+1)
    return sum(d.units for d in results.units if d.alive)