# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 06:06:36 2019

@author: gape
"""

from collections import defaultdict
import time
with open('day13.txt') as file:
    raw_data = next(file).strip().split(',')

class Program():    
    def __init__(self, hacking=False):
        self.data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))
        self.i = 0
        self.rb = 0
        if hacking:
            self.data[0] = 2
    
    def move(self, input_=0):
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
#            print(self.i, self.rb, self.data[self.i], self.data[self.i+1], self.data[self.i+2], self.data[self.i+3], values, of)
            if instruction == 1:
                self.data[self.data[self.i+3]+of] = values[0] + values[1]
            elif instruction == 2:
                self.data[self.data[self.i+3]+of] = values[0] * values[1]
            elif instruction == 3:
                self.data[self.data[self.i+1]+of] = input_
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
            
            if len(output) == 3:
                break
        return output, finish

def task1():
    hull = defaultdict(lambda: 0)
    
    p = Program()
    finish = False
    while not finish:
        output, finish = p.move()
        if finish:
            break
        x, y, z = output
        hull[(x, y)] = z
    
    return (sum([1 if c == 2 else 0 for c in hull.values()]))
                


        
def task2(display=False):
    
    def print_board():
        for (x, y), c in hull.items():
            if c == 0:
                board [y][x] = ' '
            if c == 1:
                board [y][x] = '#'
            if c == 2:
                board [y][x] = 'O'
            if c == 3:
                board [y][x] = '_'
            if c == 4:
                board [y][x] = '*'
                    
        for row in board:
            print(''.join(row))
    hull = defaultdict(lambda: 0)
    
    p = Program(hacking=True)
    finish = False
    board = [[' ' for i in range(38)] for j in range(22)]
    
    joystick = 0
    def step(joystick=0, steps=1):
        score = 0
        for i in range(steps):
            output, finish = p.move(joystick)
            if finish:
                return score, 0, 0, 0, True
            x, y, z = output
            if x == -1 and y == 0:
                score = z
            else:
                hull[(x, y)] = z
        if display:
            print_board()
        return score, x, y, z, False
    
    step(steps=838)
    d = 1
    pos_ball = 0
    ball_y = 0
    pos_player = 0
    joystick = 0
    score = 0
    while True:
        new_score, x, y ,z, finish = step(joystick, 1)
        if finish:
            break
        if new_score != 0:
            score = new_score
        if z == 4:
            if x > pos_ball:
                d = 1
            else:
                d = -1
            pos_ball = x
            ball_y = y
        if z == 3:
            pos_player = x
        
        if ball_y == 19:
            d = 0
        if pos_ball + d > pos_player:
            joystick = 1
        elif pos_ball + d < pos_player:
            joystick = -1
        else:
            joystick = 0
        if display:
            time.sleep(0.1)
    
    return score
    

