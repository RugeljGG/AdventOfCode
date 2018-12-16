# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:53:19 2018

@author: Gašper Rugelj
"""

from collections import deque

def task1():
    recipes = [3, 7]

    steps = 846021

    elves = [0, 1]
    while len(recipes) < steps + 10:
        e1 = recipes[elves[0]]
        e2 = recipes[elves[1]]
        new = str(e1+e2)
        for n in new:
            recipes.append(int(n))
        elves[0] = (elves[0] + 1 + e1) % len(recipes)
        elves[1] = (elves[1] + 1 + e2) % len(recipes)

    return (''.join(str(i) for i in recipes[steps:steps+10]))


recipes = [3, 7]

steps = 846021
steps_s = [int(i) for i in str(steps)]
sample = deque(recipes+[None for i in range(len(steps_s)-2)])

elves = [0, 1]
counter = 0

def check():
    pass

stop = False
while True:
    counter+=1
    if counter % 100000 == 0:
        print(counter, flush=True)
    e1 = recipes[elves[0]]
    e2 = recipes[elves[1]]
    new = str(e1+e2)
    for n in new:
        recipes.append(int(n))
        sample.popleft()
        sample.append(int(n))
        for i in range(len(steps_s)):
            if steps_s[i] != sample[i]:
                break
        else:
            stop = True
            break
    if stop:
        break
    elves[0] = (elves[0] + 1 + e1) % len(recipes)
    elves[1] = (elves[1] + 1 + e2) % len(recipes)
#    if steps_s in ''.join(str(i) for i in recipes[len(steps_s)-1:]):
#        break
print(len(recipes)-len(steps_s))
