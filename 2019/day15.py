# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 05:59:44 2019

@author: gape
"""

from collections import defaultdict, deque


with open('day15.txt') as file:
    raw_data = next(file).strip().split(',')

class Program():    
    def __init__(self):
        self.data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))
        self.i = 0
        self.rb = 0
    
    def move(self, input_=0):
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
                self.data[self.data[self.i+1]+of] = input_
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
    
def move(i, x, y):
    if i == 1:
        return x, y-1
    elif i ==2:
        return x, y+1
    elif i == 3:
        return x-1, y
    elif i == 4:
        return x+1, y

def print_map():
    miny = min(states.keys(), key=lambda x: x[1])[1]
    minx = min(states.keys(), key=lambda x: x[0])[0]
    maxy = max(states.keys(), key=lambda x: x[1])[1]
    maxx = max(states.keys(), key=lambda x: x[0])[0]
    
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx, maxx+1):
            try:
                c = states[(x,y)][0]
            except KeyError:
                c = 4   
            if c == 0:
                row.append('##')
            elif c == 1:
                row.append('  ')
            elif c == 2:
                row.append('XX')
            elif c == 3:
                row.append('OO')
            elif c == 4:
                row.append('EE')
        print(''.join(row))
        
        
states = dict()
queue = deque()
p = Program()
queue.append([(0,0), 0])
states[(0, 0)] = 3, [p.data.copy(), p.i, p.rb]
while len(queue):
    (x, y), c = queue.popleft()
    
    state = states[(x,y)][1]
    for i in range(1, 5):
        p.data, p.i, p.rb = state[0].copy(), state[1], state[2]
        new = move(i, x, y)
        if new in states:
            continue
        else:
            output, f = p.move(i)
#            print((x,y), new, output[0])
            if output[0] == 0:
                states[(new)] = 0, None, 0
            else:
                states[(new)] = output[0], [p.data.copy(), p.i, p.rb]
                queue.append([new, c+1])
                if output[0] == 2:
                    print("Task 1: ", c+1)
                    break

#print_map()
states = dict()
queue = deque()
queue.append([(0,0), 0])
states[(0, 0)] = 3, [p.data.copy(), p.i, p.rb]
max_c = None
while len(queue):
    (x, y), c = queue.popleft()
    
    state = states[(x,y)][1]
    for i in range(1, 5):
        p.data, p.i, p.rb = state[0].copy(), state[1], state[2]
        new = move(i, x, y)
        if new in states:
            continue
        else:
            output, f = p.move(i)
#            print((x,y), new, output[0])
            if output[0] == 0:
                states[(new)] = 0, None, 0
            else:
                states[(new)] = output[0], [p.data.copy(), p.i, p.rb]
                queue.append([new, c+1])
                if max_c is None or c+1 > max_c:
                    max_c = c+1

print("Task 2:", max_c)
    

