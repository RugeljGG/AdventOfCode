# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 07:28:05 2019

@author: gape
"""

from collections import defaultdict

with open('day9.txt') as file:
    raw_data = next(file).strip().split(',')

#raw_data = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(',')
def program(input_=1):    
    data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))
    i = 0
    rb = 0
    
    output = []
    while True:
        instruction = data[i] % 100
        if (instruction == 3 or instruction == 4 or instruction==9):
            l = 2 
        elif (instruction == 5 or instruction == 6):
            l = 3
        else: 
            l=4
        modes = [data[i] % 10**power // 10**(power-1) for power in range(3,2+l)]

        if instruction == 99:
            break
        
        values = []
        for j, m in enumerate(modes):
            if m == 0:
                values.append(data[data[i+1+j]])
            elif m == 1:
                values.append(data[i+1+j])
            elif m == 2:
                values.append(data[(data[i+1+j] + rb)])
                
        if instruction in (1,2, 7, 8):
            of = 0 if modes[2] != 2 else rb
        elif instruction in (3, ):
            of = 0 if modes[0] != 2 else rb
            
        if instruction == 1:
            data[data[i+3]+of] = values[0] + values[1]
        elif instruction == 2:
            data[data[i+3]+of] = values[0] * values[1]
        elif instruction == 3:
            data[data[i+1]+of] = input_
        elif instruction == 4:
            output.append(values[0])
        elif instruction == 5:
            if values[0] != 0:
                i = values[1]
                continue
        elif instruction == 6:
            if values[0] == 0:
                i = values[1]
                continue
        elif instruction == 7:
            if values[0] < values[1]:
                data[data[i+3]+of] = 1
            else:
                data[data[i+3]+of] = 0
        elif instruction == 8:
            if values[0] == values[1]:
                data[data[i+3]+of] = 1
            else:
                data[data[i+3]+of] = 0
        elif instruction == 9:
            rb += values[0]
        i += l
        
    return output
    
print('t1 result: ', program(1)[0])
print('t2 result: ', program(2)[0])