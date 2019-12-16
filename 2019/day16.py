# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 06:04:21 2019

@author: gape
"""

#base = [int(c) for c in '0, 1, 0, -1'.split(', ')]

#def calc(data): # slow :(
#    final = []
#    for i in range(len(data)):
#        row = []
#        for j in range(len(data)):
#            mul = base[(((j+1)//(i+1)))%len(base)]
#            c = int(data[j])
#    #        print(mul, data[j])
#            row.append(mul * c)
#    #    print(row)
#        final.append(abs(sum(row))%10)
#    return final

def calc(data):
    final = []
    for i in range(len(data)):
        j = i
        s = 0
        while j < len(data):
#            print(data[j:j+(i+1)])
            s += sum(data[j:j+(i+1)])
            j += (i+1)*2
#            print(data[j:j+(i+1)])
            s -= sum(data[j:j+(i+1)])
            j += (i+1)*2
#        print()
        final.append(abs(s)%10)
    return final

def task1():
    with open('day16.txt') as file:
        data = [int (c) for c in next(file).strip()]
    for i in range(100):
        data = calc(data)
    
    return (''.join((str(c) for c in data))[:8])
    
#repeat = set()

def task2():
    with open('day16.txt') as file:
        data = [int (c) for c in next(file).strip()]
    data = data *10000
    offset = data[:7]
    offset = int(''.join(str(c) for c in offset))
    for k in range(100):
        s = 0
        if k % 10 == 0:
            print("doing step ", k, flush=True)
        for i in range(len(data)-1, offset-1, -1):
            s += data[i] 
            data[i] = abs(s)%10

    return (''.join([str(c) for c in data])[offset:offset+8])
