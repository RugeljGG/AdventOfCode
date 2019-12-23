# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 05:59:45 2019

@author: gape
"""

from collections import defaultdict, deque, Counter



with open('day23.txt') as file:
    raw_data = next(file).strip().split(',')
    orig_data = defaultdict(lambda: 0, zip(range(len(raw_data)),(int(r) for r in raw_data)))

class Program():
    def __init__(self):
        self.data = orig_data.copy()
        self.i = 0
        self.rb = 0

    def move(self, input_=[0]):
        output = []
        finish = 0
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
                finish = 3
                break

            values = []
            for j, m in enumerate(modes):
                if m == 0:
                    values.append(self.data[self.data[self.i+1+j]])
                elif m == 1:
                    values.append(self.data[self.i+1+j])
                elif m == 2:
                    values.append(self.data[(self.data[self.i+1+j] + self.rb)])

#            print(self.i, instruction, values, modes)
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
#                    print("reading")
                    value = input_.popleft()
#                    print(value)
                    finish = 2
                    self.data[self.data[self.i+1]+of] = value
                else:
                    self.data[self.data[self.i+1]+of] = -1
                    finish = 1
#                    print("Warning, no input")
            elif instruction == 4:
                output.append(values[0])
                finish = 2
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

#            if len(output) == 1:
#                break
            break
        return output, finish

computers = []
inputs = []
outputs = []
for i in range(50):
    p = Program()
    input_ = deque([i])
    output, finish = p.move(input_)
    computers.append(p)
    inputs.append(input_)
    outputs.append(deque([]))

count = 0
nat= None
last_y = None
idle = Counter()
while True:
    done = False
    for i in range(50):
        if idle[i] > 10:
            continue
        p = computers[i]
        input_ = inputs[i]
        output, finish = p.move(input_)
        if finish == 1 and len(inputs[i]) == 0:
            idle[i]+=1
        elif finish >= 2:
            idle[i] = 0

        if len(output):
            outputs[i].append(output[0])
            if len(outputs[i]) >= 3:
                c = outputs[i].popleft()
                x = outputs[i].popleft()
                y = outputs[i].popleft()
                if c == 255:
                    if nat is None:
                        print("Task 1 answer: ", y)
                    nat = x, y
                    continue
                inputs[c].append(x)
                inputs[c].append(y)
                idle[c] = 0

    if sum(1 for i in idle.values() if i > 10) >= 50:
        if y == last_y and y != 0:
            done = True
            print("Task 2 answer: ", y)
        x, y = nat
        last_y = y
#        print(count, "sending", y)
        inputs[0].append(x)
        inputs[0].append(y)
        idle[0] = 0
    else:
        time_idle = 0
    count+=1
#    if count % 1000 == 0:
#        print(count, len(idle))
    if done:
        break
