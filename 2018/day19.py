# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:16:30 2018

@author: Gape
"""

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
with open('day19.txt') as file:
    ip = int(next(file).split(' ')[1])
    for row in file:
        row = row.split(' ')
        lines.append([row[0]] + [int(c) for c in row[1:]])
        

def task1():
    register = [0, 0, 0, 0, 0, 0]
    ipv = 0
    while ipv < len(lines):
        line = lines[ipv]
        opc = line[0]
        a, b, c = line[1:]
        register[ip] = ipv
        getattr(Opcodes, opc)(a, b, c, register)
        ipv = register[ip] + 1
        
    return register[0]
        
def task2():
    # Manual solving, printing lines and determining what's going on
    # Code sets register 2 to some high value
    # while register[3] < register[2]:
    # while register[5] <= register[2]:
    #    if register[3] * register[5] == register[2]:
    #        register[0] += register[3]
    # register[3]+=1
    # this means that register[3] wil increase until it's greater than register[2]
    # and every time register[5] % register[3] == 0, it will increase register[0] 
    # by register[1]
    register = [1, 0, 0, 0, 0, 0]
    ipv = 0
    count = 0
    while ipv < len(lines):
        line = lines[ipv]
        opc = line[0]
        a, b, c = line[1:]
        register[ip] = ipv
        getattr(Opcodes, opc)(a, b, c, register)
#        print(ipv+2, register, opc)
        ipv = register[ip] + 1
        count += 1
        if count > 50:
            break
    for line in lines:
        if line[0] == 'eqrr':
            reg = line[2]
            break
    return sum(i for i in range(1,register[reg]//2) if 10551287%i == 0) + register[reg]