# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 05:59:16 2019

@author: gape
"""

from collections import deque

with open('day7.txt') as file:
    raw_data = next(file).strip().split(',')
    
    

#raw_data = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.strip().split(',')


    
    
def program(inputs=[]):    
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
            data[data[i+1]%len(data)] = inputs.pop()
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

def task1():
    m = None
    s = []
    for a in range(5):
        for b in range(5):
            if a == b:
                continue
            for c in range(5):
                if c == a or c == b:
                    continue
                for d in range(5):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(5):
                        if e == a or e == b or e == c or e == d:
                            continue
                        ao = program([0, a])
                        bo = program([ao, b])
                        co = program([bo, c]) 
                        do = program([co, d])
                        eo = program([do, e])
                        if m is None or eo > m:
                            m = eo
                            s = [a,b,c,d,e]
    return m

class Program():
    def __init__(self, amp):
        self.data = [int(r) for r in raw_data]
        self.i = 0
        self.inputs = deque()
        self.inputs.append(amp)
    def run(self):
        data = self.data
        while True:
            instruction = data[self.i] % 100
            if (instruction == 3 or instruction == 4):
                l = 2 
            elif (instruction == 5 or instruction == 6):
                l = 3
            else: 
                l=4
            modes = [data[self.i] % 10**power // 10**(power-1) for power in range(3,2+l)]
    
            if instruction == 99:
                break
            
            values = []
            for j, m in enumerate(modes):
                if m == 0:
                    values.append(data[data[self.i+1+j] % len(data)])
                else:
                    values.append(data[self.i+1+j])
                    
            if instruction == 1:
                data[data[self.i+3]%len(data)] = values[0] + values[1]
            elif instruction == 2:
                data[data[self.i+3]%len(data)] = values[0] * values[1]
            elif instruction == 3:
                data[data[self.i+1]%len(data)] = self.inputs.pop()
            elif instruction == 4:
                self.output = values[0]
                if data[self.i+l] == 99:
                    self.i += l
                    return self.output, True
                else:
                    self.i += l
                    return self.output, False
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
                    data[data[self.i+3]%len(data)] = 1
                else:
                    data[data[self.i+3]%len(data)] = 0
            elif instruction == 8:
                if values[0] == values[1]:
                    data[data[self.i+3]%len(data)] = 1
                else:
                    data[data[self.i+3]%len(data)] = 0
            
            self.i += l
            
        return self.output, True
    

def task2():
    m = None
    s = []
    current = [None] * 5
    for a in range(5,10):
#        print('a: ', a, flush=True)
        for b in range(5,10):
            
            if a == b:
                continue
#            print('b: ', b, flush=True)
            for c in range(5,10):
                
                if c == a or c == b:
                    continue
#                print('c: ', c, flush=True)
                for d in range(5,10):
                    
                    if d == a or d == b or d == c:
                        continue
#                    print('d: ', d, flush=True)
                    for e in range(5, 10):
                        
                        if e == a or e == b or e == c or e == d:
                            continue
#                        print('e: ', e, flush=True)
                        eo = 0
                        ap = Program(a)
                        bp = Program(b)
                        cp = Program(c)
                        dp = Program(d)
                        ep = Program(e)
                        ap.inputs.appendleft(0)
                        while True:
                            ao,f1 = ap.run()
                            bp.inputs.appendleft(ao)
                            bo,f2 = bp.run()
                            cp.inputs.appendleft(bo)
                            co,f3 = cp.run()
                            dp.inputs.appendleft(co)
                            do,f4 = dp.run()
                            ep.inputs.appendleft(do)
                            eo,f5 = ep.run()
                            ap.inputs.appendleft(eo)
                            if f1 or f2 or f3 or f4 or f5:
                                break
                        if m is None or eo > m:
                            m = eo
                            s = [a,b,c,d,e]
    return m