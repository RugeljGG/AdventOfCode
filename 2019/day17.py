# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 06:03:43 2019

@author: gape
"""

from collections import defaultdict, deque
import itertools

with open('day17_t.txt') as file:
    raw_data = next(file).strip().split(',')

class Program():    
    def __init__(self, hacking=False):
        self.data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))
        self.i = 0
        self.rb = 0
        if hacking:
            self.data[0] = 2
    
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
                    print("Warning, no input")
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


p = Program()
scaf = [[]]

finish = False
while not finish:
    output, finish = p.move()
    if finish:
        break
    c = output[0] 
    if c == 10:
        scaf.append([])
    else:
        scaf[-1].append(chr(c))
  
def show():      
    for i, row in enumerate(scaf):
        print(''.join(row))
    
total = 0
start = (0, 0)
ints = set()
for y in range(1, len(scaf)-3):
    for x in range(1, len(scaf[0])-1):
        if scaf[y][x] == '#' and scaf[y+1][x] == '#' and scaf[y-1][x] == '#' and scaf[y][x+1] == '#' and scaf[y][x-1] == '#':
#            print(x, y)
            total += x*y
            ints.add((x,y))
        if scaf[y][x] == '^':
            start = x, y
            
print("Task 1: ", total, flush=True)
print()

def move(x, y, d):
    if d == 0:
        return x, y-1
    elif d == 1:
        return x+1, y
    elif d == 2:
        return x, y+1
    elif d ==3:
        return x-1, y



def find_next(x, y):
    try:
        return scaf[y][x]
    except IndexError:
        return '.'

print("Starting task 2", flush=True)
print("Calculating path", flush=True)
d = 0
finish = False
x, y = start
test = []
while True:
    nx, ny = move(x, y, d)
    nc = find_next(nx, ny)
    if nc == '#':
        x, y = nx, ny
        test.append('F')
    else:
        nx, ny = move(x, y, (d+1)%4)
        nc = find_next(nx, ny)
        if nc == '#':
            test.append('R')
            d =  (d+1) % 4
            continue
        
        nx, ny = move(x, y, (d+3)%4)
        nc = find_next(nx, ny)
        if nc == '#':
            test.append('L')
            d =  (d+3) % 4
            continue
        break

raw = ''.join(test)

s = raw

print("Calculating path compression", flush=True)
for i in range(100, 0, -1):
    s = s.replace('F'*i, str(i))

temp = s
moves = ['']
for i in range(100, 0, -1):
    l = 'L'+str(i)
    r = 'R'+str(i)
    if l in temp:
        temp = temp.replace(l, '|')
        moves.append(l)
    if r in temp:
        temp = temp.replace(r, '|')
        moves.append(r)
        
candidates = [''.join(m) for m in itertools.product(moves, moves, moves, moves, moves)]
good = []
for cand in candidates:
    if cand.count('L') + cand.count('R') < 3:
        continue
    if s.count(cand) < 2:
        continue
    good.append(cand)

finish = False
for cand1 in good:
    counter +=1
    a = s.replace(cand1, 'A')
    ca = a.count('A')
    for cand2 in good:
        b = a.replace(cand2, 'B')
        cb = b.count('B')
        if cb < 2:
            continue
        for cand3 in good:
            c = b.replace(cand3, 'C')
            cc = c.count('C')
            if len(c) == ca+cb+cc:
                finish = True
                break
        if finish:
            break
    if finish:
        break

main = c
routines = cand1,cand2,cand3
p = Program(hacking=True)
print('Giving orders', flush=True)

orders = deque([ord(c) for c in ','.join(list(main))])
orders.append(10)
while len(orders):
    o, finish = p.move(orders)
#    print(o)
  

a = 'L,10,R,8,R,12'
b = 'L,8,L,8,R,12,L,8,L,8'
c = 'L,12,L,12,R,12'

print('Giving routines', flush=True)
for routine in routines:
    r = []
    buf = []
    for i, c in enumerate(routine):
        if c in ('L', 'R'):
            if len(buf):
                r.append(''.join(buf))
                buf = []
            r.append(c)
        else:
            buf.append(c)
    if len(buf):
        r.append(''.join(buf))
    r = deque([ord(c) for c in ','.join(r)])
    r.append(10)
    
#    print(r)
    while len(r):
        o, finish = p.move(r)
#        print(o)

print('executing routines', flush=True)      
final = deque([ord('n'), 10])
while len(final):
    o, finish= p.move(final)
#    print(o)
    

new_s = [[]]

finish = False
result = 0
while not finish:
    output, finish = p.move()
    if finish:
        break
    else:
        result = output[0]
        
print("task 2: ", result)