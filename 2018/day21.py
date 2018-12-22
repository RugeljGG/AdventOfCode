# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 08:27:46 2018

@author: Gape
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:16:30 2018

@author: Gape
"""

import math

class Opcodes():
    def addr(a, b, c, reg):
        reg[c] = reg[a] + reg[b]
        
    def addi(a, b, c, reg):
        reg[c] = reg[a] + b
        
    def mulr(a, b, c, reg):
        reg[c] = reg[a] * reg[b]
    
    def muli(a, b, c, reg):
        reg[c] = reg[a] * b
        
    def banr(a, b, c, reg):
        reg[c] = reg[a] & reg[b]
    
    def bani(a, b, c, reg):
        reg[c] = reg[a] & b
        
    def borr(a, b, c, reg):
        reg[c] = reg[a] | reg[b]
        
    def bori(a, b, c, reg):
        reg[c] = reg[a] | b
        
    def setr(a, b, c, reg):
        reg[c] = reg[a]
        
    def seti(a, b, c, reg):
        reg[c] = a
        
    def gtir(a, b, c, reg):
        reg[c] = int(a > reg[b])
        
    def gtri(a, b, c, reg):
        reg[c] = int(reg[a] > b)
        
    def gtrr(a, b, c, reg):
        reg[c] = int(reg[a] > reg[b])
        
    def eqir(a, b, c, reg):
        reg[c] = int(a == reg[b])
        
    def eqri(a, b, c, reg):
        reg[c] = int(reg[a] == b)
        
    def eqrr(a, b, c, reg):
        reg[c] = int(reg[a] == reg[b])
        

lines = []
with open('day21.txt') as file:
    ip = int(next(file).split(' ')[1])
    for row in file:
        row = row.split(' ')
        lines.append([row[0]] + [int(c) for c in row[1:]])
        


def task1():
    register = [0, 0, 0, 0, 0, 0]
    ipv = 0
    counter = 0
    while ipv < len(lines):
        line = lines[ipv]
        opc = line[0]
        a, b, c = line[1:]
        register[ip] = ipv
    #    print(ipv+2, register, opc)
        if opc == 'eqrr':
            return register[4]
        getattr(Opcodes, opc)(a, b, c, register)
        ipv = register[ip] + 1
        counter += 1
    
def task2(start=0):
    r4 = start
    rank = 0
    previous = dict()
    while True:
        rank+=1
        r5 = 65536 | r4
        r4 = 10704114
        for i in range(int(math.log(r5, 256))+1):
            
            r2 = r5 & 255
            r4 = r2 + r4
            r4 = r4 * 65899
            r4 = r4 & 16777215
            r5 = r5 // 256
        if r4 in previous:
            break
        else:
            previous[r4] = rank
    return max(previous.items(), key=lambda x: x[1])[0]