# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 05:58:16 2019

@author: gape
"""

from collections import defaultdict

with open('day11.txt') as file:
    raw_data = next(file).strip().split(',')

class Program():    
    def __init__(self):
        self.data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))
        self.i = 0
        self.rb = 0
    
    def move(self, input_):
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
            
            if len(output) == 2:
                break
        return output, finish
  
    

def move(x, y, d):
    if d == 0:
        return x+0, y+1
    elif d == 1:
        return x+1, y
    elif d == 2:
        return x+0, y-1
    elif d == 3:
        return x-1, y
   
def task1():
    hull = defaultdict(lambda: 0)
    
    p = Program()
    finish = False
    x, y = 0, 0
    d = 0
    while not finish:
        output, finish = p.move(hull[(x, y)])
        if finish:
            break
        hull[(x, y)] = output[0]
        d = (d -1 + output[1] * 2) % 4
        x, y = move(x, y, d)
    
    return len(hull)
            

def task2():
    hull = defaultdict(lambda: 0)
    
    p = Program()
    finish = False
    x, y = 0, 0
    d = 0
    hull[(x,y)] = 1
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    while not finish:
        output, finish = p.move(hull[(x, y)])
        if finish:
            break
        hull[(x, y)] = output[0]
        d = (d -1 + output[1] * 2) % 4
        x, y = move(x, y, d)
        
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    

    b = [[' ' if hull[(x,y)] == 0 else '#' for x in range(min_x-1, max_x +2)] for y in range(min_y-1, max_y+2)]
    for row in b[::-1]:
        print(''.join(row))
