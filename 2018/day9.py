# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 06:28:44 2018

@author: Gape
"""

from collections import defaultdict
import pandas as pd
import re
import time


with open('day_9.txt') as file:
    data = next(file)
    r = re.findall('(.*?) players; last marble is worth(.*?) points', data)
    players = int(r[0][0])
    marbles = int(r[0][1])


def task1(players, marbles):
    l = [0]
    i = 1
    p = 0
    scores = defaultdict(int)
    latest = time.time()
    for m in range(1, marbles+1):
        if m % 50000 == 0:
            duration = time.time() - latest
            print(m, duration)
            latest = time.time()
        p = p % players + 1
        if m % 23 == 0:
            scores[p] += m
            i-=7
            if i<0:
                i+=1
            scores[p] += l.pop(i)
        else:
            i+=2
            i = i % len(l)
            l.insert(i, m)
            scores[p]+=0
#        a = l.copy()
#        a[i] = '_{}_'.format(a[i])
#        print(p, a)

    return max(scores.values())

def task2(players, marbles):
    class Marble():
        def __init__(self, m, p, n):
            self.m = m
            self.p = p
            self.n = n   

    i = 1
    p = 0
    scores = defaultdict(int)
    latest = time.time()
    marble = Marble(0, None, None)
    marble.p = marble
    marble.n = marble
    
    for m in range(1, marbles+1):
        new = Marble(m, None, None)
        if m % 500000 == 0:
            duration = time.time() - latest
            print(m, duration)
            latest = time.time()
        p = p % players + 1
        if m % 23 == 0:
            scores[p] += m
            for i in range(6):
                marble = marble.p
            scores[p] += marble.p.m
            marble.p = marble.p.p
            marble.p.n = marble
        else:
            new.p = marble.n
            new.n = marble.n.n
            new.n.p = new
            new.p.n = new
            marble = new
    
    return max(scores.values())

