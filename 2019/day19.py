# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:00:24 2019

@author: gape
"""

from collections import defaultdict, deque, Counter
import itertools

with open('day19.txt') as file:
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
                    self.data[self.data[self.i+1]+of] = 0
#                    print("Warning, no input")
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

def part1():
    a = Counter()
    for x in range(50):
        for y in range(50):
            p = Program()
            coords = deque((x,y))
            output, finish = p.move(coords)
            a[output[0]]+=1
    
    return a[1]
def part2():
    mx = 1
    x = 0
    y = 50
    w = 0
    heights = defaultdict(lambda: 0)
    r_count = 0
    while True:
    #    print(x,y)
        p = Program()
        coords = deque((x,y))
        output, finish = p.move(coords)
        if output[0] == 1:
            if heights[y] < x:
                heights[y] = x
            if r_count == 0:
                x += 99
                r_count = 1
            elif r_count == 1:
                if x-mx >= 99 and heights[y-99] >= x:
                    break
                else:
                    x = mx + w-1
                    r_count = 2
            elif r_count == 2:
                x+=1
        else:
            if y in heights:
                w = x - mx
                y+=1
                x = mx
                r_count = 0
            else:
                x+=1
                mx = x
                    
    return (x-99) * 10000 + y - 99


print("Task 1: ", part1())
print("Task 2: ", part2())