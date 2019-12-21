# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 05:58:51 2019

@author: gape
"""

from collections import defaultdict, deque, Counter
import itertools


    
with open('day21.txt') as file:
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


instructions_1 = [
'NOT A T',
'NOT B J',
'OR T J',
'NOT C T',
'OR T J',
'AND D J',
'WALK',
'\n']

instructions_2 = [
'NOT A T',
'NOT B J',
'OR T J',
'NOT C T',
'OR T J',
'AND D J',
'NOT J T',
'OR E T',
'OR H T',
'AND T J',
'RUN',
'\n']

def run_program(instructions):
    insts = deque((ord(c) for c in  '\n'.join(instructions)))
    p = Program()
    finish = False
    output = []
    count = 0
    while not finish:
        count += 1
        o, finish = p.move(insts)
        if finish:
            break
        output.append(o[0])
    if output[-1] > 150:
        return output[-1]
    else:
        print("Failed :(")
        print(count)
        print(''.join(chr(c) for c in output))
        
print("Task 1: ", run_program(instructions_1))
print("Task 2: ", run_program(instructions_2))