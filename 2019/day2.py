# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 05:54:30 2019

@author: gape
"""
with open('day2.txt') as file:
    raw_data = next(file).strip().split(',')

def task1(a=12, b=2):    
    data = [int(r) for r in raw_data]
    data[1] = a
    data[2] = b
    i = 0
    while True:
        if data[i] == 99:
            break
        elif data[i] == 1:
            p = data[i+3] % len(data)
            p1 = data[i+1] % len(data)
            p2 = data[i+2] % len(data)
            data[p] = data[p1] + data[p2]
        elif data[i] == 2:
            p = data[i+3] % len(data)
            p1 = data[i+1] % len(data)
            p2 = data[i+2] % len(data)
            data[p] = data[p1] * data[p2]
        i += 4
        
    return data[0]
    
def task2(output=19690720):
    for noun in range(5):
        for verb in range(5):
            print(task1(noun, verb))
        
    # manually see that noun increases data by 240000, verb by 1
    # numbers start at 10694
    
    noun = output // 240000
    verb = output % 240000 - 10694
    # check for edge cases just in case :)
    for n in range(noun-1, noun+2):
        for v in range(verb-1, verb+2):
            if task1(noun, verb) == output:    
                return noun*100+verb