# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 06:57:48 2019

@author: gape
"""

from collections import defaultdict, deque
from itertools import combinations
import re



with open('day25.txt') as file:
    raw_data = next(file).strip().split(',')
    orig_data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))

class Program():
    def __init__(self):
        self.data = orig_data.copy()
        self.i = 0
        self.rb = 0

    def move(self, input_=[0]):
        output = []
        finish = False
        while True:
            instruction = self.data[self.i] % 100
            if (instruction == 3 or instruction == 4 or instruction==9):
                l = 2
            elif (instruction == 5 or instruction == 6):
                l = 3
            else:
                l=4
            modes = [self.data[self.i] % 10**power // 10**(power-1) for power in range(3,2+l)]

            if instruction == 99:
                finish = True
                break

            values = []
            for j, m in enumerate(modes):
                if m == 0:
                    values.append(self.data[self.data[self.i+1+j]])
                elif m == 1:
                    values.append(self.data[self.i+1+j])
                elif m == 2:
                    values.append(self.data[(self.data[self.i+1+j] + self.rb)])

#            print(self.i, instruction, values, modes)
            if instruction in (1,2, 7, 8):
                of = 0 if modes[2] != 2 else self.rb
            elif instruction in (3, ):
                of = 0 if modes[0] != 2 else self.rb
            else:
                of = 0
            if instruction == 1:
                self.data[self.data[self.i+3]+of] = values[0] + values[1]
            elif instruction == 2:
                self.data[self.data[self.i+3]+of] = values[0] * values[1]
            elif instruction == 3:
                if len(input_):
                    value = input_.popleft()
#                    print(value)
                    self.data[self.data[self.i+1]+of] = value
#                    print("reading")
                else:
                    return output, 8
            elif instruction == 4:
                output.append(values[0])
            elif instruction == 5:
                if values[0] != 0:
                    self.i = values[1]
                    continue
            elif instruction == 6:
                if values[0] == 0:
                    self.i = values[1]
                    continue
            elif instruction == 7:
                if values[0] < values[1]:
                    self.data[self.data[self.i+3]+of] = 1
                else:
                    self.data[self.data[self.i+3]+of] = 0
            elif instruction == 8:
                if values[0] == values[1]:
                    self.data[self.data[self.i+3]+of] = 1
                else:
                    self.data[self.data[self.i+3]+of] = 0
            elif instruction == 9:
                self.rb += values[0]
            self.i += l

            if len(output) == 1:
                break
        return output, finish


p = Program()

rooms = dict()
class Room():
    def __init__(self, name, directions, orig='down'):
        self.neighbours = dict()
        self.name = name
        self.orig = orig
        self.directions = directions

    def spread(self):
        if self.name == 'Security Checkpoint':
#            print ("---- found Security, moving back")
            output = move(self.orig)
            return [self.name]
        final = None
#        print(self.directions)
        for d in self.directions:
#            print(self.name, d)
            if d != self.orig:
#                print ("---- Moving "+d)
                output = move(d)
                name, directions, items = parse(output)
                self.neighbours[name] = d
                for i in items:
                    if i in forbidden_items:
                        continue
#                    print('------ Taking item ', i)
                    output = move('take '+i)
                if name in rooms:
                    room = rooms[name]
                else:
                    room = Room(name, directions, reverse[d])
                    rooms[name] = room
                    room.neighbours[self.name] = reverse[d]
                    r = room.spread()
                    if r is not None:
#                        final = ' '.join((self.name, r))
                        final = [self.name] + r
#                        print(" --- WAY = ", final )
        if self.orig != 'down':
#            print ("---- Moving back "+self.orig)
            output = move(self.orig)
#        print(final)
        return final



def move(command, debug=False):
    input_ = deque([ord(c) for c in command])
    input_.append(10)
    output=[]
    while True:
        o, finish = p.move(input_)
        if finish == 3 or finish == 8:
            break
        try:
            output.append(o[0])
        except:
            return output
    if debug:
        try:
            print(''.join(chr(c) for c in output))
        except:
            print("Error printing")
    return output
#    return

def parse(output):
    s = ''.join(chr(c) for c in output)
    name = re.findall('==(.*?)==', s)
    if len(name):
        name = name[0].strip()
    else:
        name = None
    stuff = re.findall('\n- (.*?)(?=\n)', s)
    directions = []
    items = []
    for thing in stuff:
        if thing in ('north', 'south', 'west', 'east'):
            directions.append(thing)
        else:
            items.append(thing)
    return name, directions, items

forbidden_items = 'infinite loop', 'giant electromagnet', 'escape pod', 'molten lava', 'photons'
reverse = {'north': 'south',
           'south': 'north',
           'east': 'west',
           'west': 'east',
           'down':'up'}

output = move('inv')
name, directions, items = parse(output)
room = Room(name, directions)
rooms[name] = room
final = room.spread()

print("Found all items, moving to security checkpoint and trying item combinations")

for f in final[1:]:
    d = room.neighbours[f]
    move(d)
    room = rooms[f]

output = move('inv')
_, _, items = parse(output)

for item in items:
    move('drop '+item)

heavy = 'A loud, robotic voice says "Alert! Droids on this ship are heavier than the detected value!" and you are ejected back to the checkpoint.'
light = 'A loud, robotic voice says "Alert! Droids on this ship are lighter than the detected value!" and you are ejected back to the checkpoint.'

exceed = []
done = False
for i in range(len(items)):
    for comb in combinations(items, i):
        t = set(comb)

        if any((e.issubset(t) for e in exceed)):
            continue

        for item in comb:
            move('take '+item, debug=False)
        output = move('west', debug=False)
        s = ''.join(chr(c) for c in output)
        if light in s:
            exceed.append(t)
        elif heavy not in s:
            done = True
            break
        for item in comb:
            move('drop '+item, debug=False)


    if done:
        break

#print(s)
print("Task 1 answer: ", re.findall('\d+', s)[0])