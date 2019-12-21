# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 05:59:50 2019

@author: gape
"""

from collections import defaultdict, deque
import itertools

       
class Point():
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.hn = defaultdict(lambda: None)
        self.neighbours = defaultdict(lambda: None)
                      
    def spread(self, state, movers, points, target=26):
        x, y = self.x, self.y
        n = self.hn.pop(state)
        state = set(state)
        if self.c.islower():
            state.add(self.c)
        frozen = frozenset(state)
        self.hn[frozen] = n
        if len(frozen) >= target:
            return n
        for ns in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            nb = points[ns]
            if nb.c != '#':
                if nb.c.isupper() and nb.c.lower() not in frozen:
                    continue
                better = False
                for key in nb.hn.keys():
                    if frozen.issubset(key):
                        if n+1 >= nb.hn[key]:
                            better = True
                            break
                if better:
                    continue
                worse = set()
                for key in nb.hn.keys():
                    if key.issubset(frozen):
                        if n+1 <= nb.hn[key]:
                            worse.add(key)
                for w in worse:
                    nb.hn.pop(w)
                nb.hn[frozen] = n+1
                movers.append((nb,frozen))
        return False
        
        
    def spread_fast(self, state, movers, heroes, steps):
#        n = self.hn.pop(state)
        for p, dist in self.neighbours.items():
            new_state = set(state)
            if p == self.c:
                continue
            nb = heroes[p]
            if nb.c.isupper() and nb.c.lower() not in new_state:
                continue
            elif nb.c.islower():
                new_state.add(nb.c)
            better = False
            for key in nb.hn.keys():
                if new_state.issubset(key):
                    if steps+dist >= nb.hn[key]:
                        better = True
                        break
            if better:
                continue
            worse = set()
            for key in nb.hn.keys():
                if key.issubset(new_state):
                    if steps+dist <= nb.hn[key]:
                        worse.add(key)
            for w in worse:
                nb.hn.pop(w)
            frozen = frozenset(new_state)
            nb.hn[frozen] = steps+dist
            movers.append((nb,frozen, steps+dist))

            
    def find_neighbours(self, p, n, points):
        x, y = self.x, self.y
        if self.neighbours[p] is None or self.neighbours[p] > n:
            if p != self.c:
                self.neighbours[p] = n
            if self.c == '.' or p == self.c:
                for ns in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
                    nb = points[ns]
                    if nb.c != '#':
                        nb.find_neighbours(p, n+1, points)
        
    def __repr__(self):
        return self.c +' ({},{})'.format(self.x, self.y)

def task1_slow():
    lab = []
    with open('day18.txt') as file:
        for row in file:
            lab.append([c for c in row.strip()])
    
    points = dict()
    possible_keys = set()
    for y in range(len(lab)):
        for x in range(len(lab[0])):
            p = Point(x, y, lab[y][x])
            points[(x,y)] = p
            if p.c == '@':
                xs, ys = x, y
            elif p.c.islower():
                possible_keys.add(p.c)
    
    target = len(possible_keys)
    state = frozenset()
    movers = deque()
    points[xs, ys].hn[state] = 0
    movers.append((points[xs, ys], state))
    best = None
    while movers:
        if best is None:
            n, state = movers.pop()
        else:
            n, state = movers.popleft()
        
        if best is not None and n.hn[state] >= best:
            continue    
        finish = n.spread(state, movers, points, target=target)
        if finish:
            if best is None or finish < best:
                print(finish, flush=True)
                best = finish
    print("Task 1 answer: ", best)


def task1():
    lab = []
    with open('day18.txt') as file:
        for row in file:
            lab.append([c for c in row.strip()])
    
    points = dict()
    heroes = dict()
    possible_keys = set()
    for y in range(len(lab)):
        for x in range(len(lab[0])):
            p = Point(x, y, lab[y][x])
            points[(x,y)] = p
            if p.c not in ('#', '.'):
               heroes[p.c] = p
            if p.c == '@':
                xs, ys = x, y
            elif p.c.islower():
                possible_keys.add(p.c)
    
    for hero in heroes.values():
        hero.find_neighbours(hero.c, 0, points)
        hero.neighbours.pop(hero.c)
        
    target = len(possible_keys)
    state = frozenset()
    movers = deque()
    points[xs, ys].hn[state] = 0
    movers.append((points[xs, ys], state, 0))
    best = None
    while movers:
        n, state, steps = movers.popleft()
        if len(state) >= target:
            if best is None or n.hn[state] < best:
                best = n.hn[state]
#                return best
        if best is not None and n.hn[state] >= best:
            continue
        n.spread_fast(state, movers, heroes, steps)
    return best


def task2():
    lab = []
    with open('day18_2.txt') as file:
        for row in file:
            lab.append([c for c in row.strip()])
    
    points = dict()
    heroes = dict()
    starters = dict()
    possible_keys = set()
    for y in range(len(lab)):
        for x in range(len(lab[0])):
            p = Point(x, y, lab[y][x])
            points[(x,y)] = p
#            if p.c in ('0', '1', '2', '3'):
            if p.c == '@':
                p.c = str(len(starters))
                starters[p.c] = p
            if p.c not in ('#', '.'):
               heroes[p.c] = p
            if p.c.islower():
                possible_keys.add(p.c)
    
    
    for hero in heroes.values():
        hero.find_neighbours(hero.c, 0, points)
        hero.neighbours.pop(hero.c)

    state = frozenset()
    new_states = deque()
    first_move = []
    positions = []
    for starter in starters.values():
        starter.hn[state] = 0
        first_move.append(deque([(starter, state)]))
        positions.append(starter.c)
    states = dict()
    new_states.append(((state, ''.join(positions), 0), 0))
    best = None
    target = len(possible_keys)
    while len(new_states):
        (old_state, positions, i), old_steps = new_states.pop()
        if best is not None and old_steps > best:
            continue
        for i, p in enumerate(positions):
            to_clear = set()
            old_pos = [p for p in positions]
            n = heroes[p]
            n.hn[old_state] = old_steps
            movers = deque([(n, old_state, old_steps)])
            candidates = dict()
            while movers:
                n, state, steps = movers.popleft()
                if len(state) >= target:
                    if best is None or n.hn[state] < best:
                        best = n.hn[state]
                    continue
#                        print(best)                   
                old_pos[i] = n.c
                key = state, ''.join(old_pos), i
                if key in states and states[key] <= steps:
                    continue
                elif len(state) > len(old_state):
                    if state not in candidates or candidates[state][1]>steps:
                        candidates[state] = key, steps
                    
                n.spread_fast(state, movers, heroes, steps)
                to_clear.add(n)
            for key, steps in candidates.values():
                states[key] = steps
                new_states.append(((key), steps))
            for n in to_clear:
                n.hn.clear()
    return best

print("Task 1: ", task1())
print("Task 2: ", task2())