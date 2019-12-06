# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:53:34 2019

@author: gape
"""

from collections import defaultdict

class Planet():
    def __init__(self):
        self.orbits = []
        self.orbited_by = []
        self.santa = False
    
    def count_orbits(self):
        return len(self.orbits) + sum([p.count_orbits() for p in self.orbits])
    
    def plant_santa(self, i):
        self.santa = i
        for p in self.orbits:
            p.plant_santa(i+1)
            
    def find_santa(self, i):
        if self.santa:
            return self.santa + i
        else:
            return min((p.find_santa(i+1) for p in self.orbits))
            
def task1():
    planets = defaultdict(lambda: Planet())
    
    with open('day6.txt') as file:
        for row in file:
            p1, p2 = row.strip().split(')')
            planets[p1].orbited_by.append(planets[p2])
            planets[p2].orbits.append(planets[p1])
            
    return sum((p.count_orbits() for p in planets.values()))

def task2():
    planets = defaultdict(lambda: Planet())
    
    with open('day6.txt') as file:
        for row in file:
            p1, p2 = row.strip().split(')')
            planets[p1].orbited_by.append(planets[p2])
            planets[p2].orbits.append(planets[p1])
            
    planets['SAN'].plant_santa(-1)
    return planets['YOU'].find_santa(-1)
    