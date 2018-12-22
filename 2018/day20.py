# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:14:27 2018

@author: Gape
"""


#data = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'
with open('day20.txt') as file:
    data = next(file).strip()

def move(d, x, y):
    if d == 'N':
        y-=2
    elif d == 'E':
        x+=2
    elif d == 'S':
        y+=2
    elif d == 'W':
        x-=2
    return x, y


class Room():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = dict()
        self.value = None
        self.taken = set()
        
    def travel_value(self):
#        self.value = value
        value = self.value
        for n in self.neighbours.values():
            if n.value is None or n.value > value+1:
                n.value = value+1
                to_value.append(n)
        
    def travel(self, data):
        self.taken.add(data)
        x, y = self.x, self.y
        for s in split(data):
            if s != '$':
                d = s[0]
                coords = move(d, x, y)
                if coords in rooms.keys():
                    room = rooms[coords]
                    room.neighbours[opposite[d]] = self
                    break
                else:
                    room = Room(*coords)
                    rooms[coords] = room
                self.neighbours[d] = room
                room.neighbours[opposite[d]] = self
                to_travel.append((room, s[1:]))
    
    def __repr__(self):
        return '({}, {}); Neighbours: {}'.format(self.x, self.y, ', '.join(self.neighbours.keys()))

def split(s):
    n = s[0]
    if n == '(':
        groups = []
        current = []
        c = 1
        i = 0
        while c > 0:
            i += 1
            if s[i] == '(':
                c += 1
            elif s[i] == ')':
                c -= 1
            elif s[i] == '|' and c == 1:
                groups.append(current)
                current = []
                continue
            current.append(s[i])
        groups.append(current[:-1])
    
        return [x for group in groups for x in split(''.join(group)+s[i+1:])]
            
    else:
        return [s]

opposite = {'N' : 'S',
             'W' : 'E',
             'S' : 'N',
             'E' : 'W'}          
special = []         
rooms = dict()

start = Room(0, 0)
rooms[(0,0)] = start
to_travel = [(start, data[1:])]
while to_travel:
    room, s = to_travel.pop()
    room.travel(s)

minx = None
miny = None
maxx = None
maxy = None
for x, y in rooms.keys():
    if minx is None or x < minx:
        minx = x
    if maxx is None or x > maxx:
        maxx = x
    if miny is None or y < miny:
        miny = y
    if maxy is None or y > maxy:
        maxy = y
        
zone = [['#' for x in range(maxx-minx+3)] for y in range(maxy-miny+3)]

for room in rooms.values():
    x, y = room.x-minx+1, room.y-miny+1
    zone[y][x] = '.'
    for c in room.neighbours.keys():
            if c == 'N':
                zone[y-1][x] = '-'
            elif c == 'E':
                zone[y][x+1] = '|'
            elif c == 'S':
                zone[y+1][x] = '-'
            elif c == 'W':
                zone[y][x-1] = '|'
  
start.value = 0
to_value = [start]              
while to_value:
    room = to_value.pop()
    room.travel_value()


print(max(rooms.values(), key=lambda x: x.value).value)
print(sum(1 if room.value >= 1000 else 0 for room in rooms.values()))