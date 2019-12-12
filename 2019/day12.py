# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 06:07:15 2019

@author: gape
"""


from math import gcd
import re

class Moon():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        
    def energy(self):
        p = abs(self.x) + abs(self.y) + abs(self.z)
        k = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return p*k
    
    def __repr__(self):
        x,y,z,vx,vy,vz = self.x, self.y, self.z, self.vx, self.vy, self.vz
        return "pos=<x={}, y=  {}, z= {}>, vel=<x= {}, y= {}, z= {}>".format(x,y,z,vx,vy,vz)
    
def task1(num=1000):

    moons = []
    with open('day12.txt') as file:
        for row in file:
            x, y, z = (int(c) for c in re.findall('(\-?\d+)', row))
            moons.append(Moon(x, y, z))
#    for moon in moons:
#        print(moon)
    for t in range(num):
        x = sorted(moons, key= lambda x: x.x)
        y = sorted(moons, key= lambda x: x.y)
        z = sorted(moons, key= lambda x: x.z)
        
        for moon1 in moons:
            for moon2 in moons:
                if moon1.x<moon2.x:
                    moon1.vx +=1
                elif moon1.x>moon2.x:
                    moon1.vx -=1
                
                if moon1.y<moon2.y:
                    moon1.vy +=1
                elif moon1.y>moon2.y:
                    moon1.vy -=1
                    
                if moon1.z<moon2.z:
                    moon1.vz +=1
                elif moon1.z>moon2.z:
                    moon1.vz -=1
        
        for moon in moons:
            moon.move()
    #        print(moon)
            
            
    return print(sum(moon.energy() for moon in moons))


def task2(num=1000000):

    moons = []
    with open('day12.txt') as file:
        for row in file:
            x, y, z = (int(c) for c in re.findall('(\-?\d+)', row))
            moons.append(Moon(x, y, z))
#    for moon in moons:
#        print(moon)
    
    px = dict()
    py = dict()
    pz = dict()
    for t in range(num):
        x = sorted(moons, key= lambda x: x.x)
        y = sorted(moons, key= lambda x: x.y)
        z = sorted(moons, key= lambda x: x.z)
        
        for moon1 in moons:
            for moon2 in moons:
                if moon1.x<moon2.x:
                    moon1.vx +=1
                elif moon1.x>moon2.x:
                    moon1.vx -=1
                
                if moon1.y<moon2.y:
                    moon1.vy +=1
                elif moon1.y>moon2.y:
                    moon1.vy -=1
                    
                if moon1.z<moon2.z:
                    moon1.vz +=1
                elif moon1.z>moon2.z:
                    moon1.vz -=1
        
        for moon in moons:
            moon.move()
    #        print(moon)
        

        multiples = [0, 0, 0]
        xs = tuple((moon.x, moon.vx) for moon in moons)
        if xs in px:
#            print(t- px[xs], 'x')
            multiples[0] = t- px[xs]
        px[xs] = t
        
        ys = tuple((moon.y, moon.vy) for moon in moons)
        if ys in py:
#            print(t- py[ys], 'y')
            multiples[1] = t- py[ys]
        py[ys] = t
            
        zs = tuple((moon.z, moon.vz) for moon in moons)
        if zs in pz:
#            print(t- pz[zs], 'z')
            multiples[2] = t- pz[zs]
        pz[zs] = t
        
        if min(multiples)>0:
            break
        
    x, y, z = multiples
    a = int(x*y/gcd(x, y))
    return a*z/gcd(a,z)