# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 06:18:30 2019

@author: gape
"""


with open('day5.txt') as file:
    raw_data = next(file).strip().split(',')

def task1(input_=1):    
    data = [int(r) for r in raw_data]
    i = 0
    
    while True:
        instruction = data[i] % 100
        if (instruction == 3 or instruction == 4):
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
                values.append(data[data[i+1+j] % len(data)])
            else:
                values.append(data[i+1+j])
                
        if instruction == 1:
            data[data[i+3]%len(data)] = values[0] + values[1]
        elif instruction == 2:
            data[data[i+3]%len(data)] = values[0] * values[1]
        elif instruction == 3:
            data[data[i+1]%len(data)] = input_
        elif instruction == 4:
            output = values[0]
            if output != 0:
                if data[i+l] == 99:
                    return output
                else:
                    return i, "narobe"
        
        i += l
        
    return output
    


def task2(input_=5):    
    data = [int(r) for r in raw_data]
    i = 0
    
    while True:
        instruction = data[i] % 100
        if (instruction == 3 or instruction == 4):
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
                values.append(data[data[i+1+j] % len(data)])
            else:
                values.append(data[i+1+j])
                
        if instruction == 1:
            data[data[i+3]%len(data)] = values[0] + values[1]
        elif instruction == 2:
            data[data[i+3]%len(data)] = values[0] * values[1]
        elif instruction == 3:
            data[data[i+1]%len(data)] = input_
        elif instruction == 4:
            output = values[0]
            if output != 0:
                if data[i+l] == 99:
                    return output
                else:
                    return i, "narobe"
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
                data[data[i+3]%len(data)] = 1
            else:
                data[data[i+3]%len(data)] = 0
        elif instruction == 8:
            if values[0] == values[1]:
                data[data[i+3]%len(data)] = 1
            else:
                data[data[i+3]%len(data)] = 0
        
        i += l
        
    return output
    