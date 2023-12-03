# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:12:16 2020

@author: gape
"""

import requests

with open('../token.txt', 'r') as file:
    token = next(file)
    
url = 'https://adventofcode.com/2015/day/1/input'
r = requests.get(url, cookies={'session':token})

data = r.text
with open('day1.txt', 'w') as file:
    print(r.text, file=file)

print('Day 1 input:')
print(data)
print('\nTotal input length: ', len(data))

i = 0
j = 0
for c in data:
    j+=1
    if c == '(':
        i+=1
    else:
        i-=1
    if i == -1:
        print(j)
        break