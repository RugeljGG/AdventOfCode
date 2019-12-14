# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 06:01:12 2019

@author: gape
"""

from collections import defaultdict

class Material():
    def __init__(self, q):
        self.requires = []
        self.q = q
        self.n = 0
        self.count = 0
        self.built = 0

    def give(self, n):
        if len(self.requires):
            while self.n < n:
                num = (n-self.n) // self.q
                if (n-self.n) % self.q != 0:
                    num += 1
                for m, q in self.requires.items():
                    m.give(q*num)
                self.n += self.q * num
            self.n -= n
        self.count += n 
        
def task1():         
    materials = defaultdict(lambda: Material(1))
    with open('day14.txt') as file:
        for row in file:
            rows = row.strip().split(' => ')
            mats = []
            for c in rows[0].split(', '):
                mats.append(c.split(' '))
            requires = {materials[mat[1]]: int(mat[0]) for mat in mats}
            num, name = rows[1].split(' ')
            num = int(num)
            m = materials[name]
            m.q = num
            m.requires = requires
            
    materials['FUEL'].give(1)
    return materials['ORE'].count


def task2(n=1000000000000):
    materials = defaultdict(lambda: Material(1))
    with open('day14_t.txt') as file:
        for row in file:
            rows = row.strip().split(' => ')
            mats = []
            for c in rows[0].split(', '):
                mats.append(c.split(' '))
            requires = {materials[mat[1]]: int(mat[0]) for mat in mats}
            num, name = rows[1].split(' ')
            num = int(num)
            m = materials[name]
            m.q = num
            m.requires = requires
    
    materials['FUEL'].give(1)
    cca = n // materials['ORE'].count
    materials['FUEL'].give(cca)
    k = n / materials['ORE'].count
    t = int(materials['FUEL'].count * (k-1))
    materials['FUEL'].give(t-5)
    while materials['ORE'].count < n:
        materials['FUEL'].give(1)    
    return materials['FUEL'].count - 1