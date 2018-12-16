# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:21:43 2018

@author: Gape
"""

from  collections import defaultdict
import re



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
        

samples = []
real = []
with open('day16.txt') as file:
    while True:
        before = next(file).strip()
        if before == '':
            break
        instruction = next(file).strip()
        after = next(file).strip()
        next(file)
        
        before = [int(c) for c in re.findall('\[(\d), (\d), (\d), (\d)\]', before)[0]]
        instruction = [int(c) for c in instruction.split(' ')]
        after = [int(c) for c in re.findall('\[(\d), (\d), (\d), (\d)\]', after)[0]]

        samples.append([before, instruction, after])
    for row in file:
        row = row.strip()
        if row == '':
            continue
        real.append([int(c) for c in row.split(' ')])



#before = [3, 2, 1, 1]
#instruction = 9, 2, 1, 2
#after = [3, 2, 2, 1]

def task1():
    confusing = 0
    for sample in samples:
        before, instruction, after = sample
        counter = 0
        for name, f in Opcodes.__dict__.items():
            if name[0] == '_':
                continue
            else:
                new = before.copy()
                f(*instruction[1:], new)
        #        print(name, new)
                if new == after:
                    counter += 1
        
        if counter >= 3:
            confusing += 1
    
    return confusing

def task2():
    codes = dict()
    used = set()
    while len(codes) < 16:
        for sample in samples:
            before, instruction, after = sample
            counter = 0
            possible = []
            opcode = instruction[0]
            if opcode in codes.keys():
                continue
            for name, f in Opcodes.__dict__.items():
                if name[0] == '_' or name in used:
                    continue
                else:
                    new = before.copy()
                    f(*instruction[1:], new)
            #        print(name, new)
                    if new == after:
                        possible.append([name, f])
            if len(possible) == 1:
    #            print(instruction, opcode, possible[0][0])
                codes[opcode] = possible[0][1]
                used.add(possible[0][0])
                
    register = [0, 0, 0, 0]
    for instruction in real:
        opcode = instruction[0]
        codes[opcode](*instruction[1:], register)